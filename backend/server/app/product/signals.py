from pprint import pprint

from django.core.exceptions import ValidationError
from django.dispatch import receiver
from django.dispatch import Signal
from django.db.models import Count, Q
from django.db.models import Sum, Min


from app.product.models import Product, ProductItem, VariationOption, Price
 
my_signal = Signal()


def validate_variations(variation_pk_set):
    new_variations = VariationOption.objects.filter(pk__in=variation_pk_set).values_list('variation_id', flat=True)
    if len(set(new_variations)) != len(new_variations):
        raise ValidationError("Duplicate variation detected in Options.")


def check_elements_exist(elements, lst):
    lst_set = set(lst)
    return all(element in lst_set for element in elements)


def validate_prices(prices):
    new_prices = prices.values_list("currency_id", flat=True)

    if len(set(new_prices)) != len(new_prices):
        raise ValidationError("Duplicate prices detected in Options.")
    if not check_elements_exist([1,4], new_prices):
        raise ValidationError("The currencies must be set to USD, RUB.")


def get_min_price_product_item_id(variations):
    variations_list = []
    if isinstance(variations, (list, tuple)):
        variations_list.extend(variations)
    else:
        variations_list.append(variations)

    variations_len = len(set(variations_list))

    # WITH summed_values AS (
    #     SELECT product_price.product_id, SUM(value) AS total_value, product_productitem.date_added AS date_added
    #     FROM product_price
    #     JOIN product_productitem ON product_price.product_id = product_productitem.id
    #     GROUP BY product_price.product_id
    #     ORDER BY date_added
    # )
    # SELECT product_id, total_value, date_added
    # FROM summed_values
    # WHERE total_value = (SELECT MIN(total_value) FROM summed_values);

    # exact match m2m
    # Получаем объекты ProductItem, соответствующие условиям
    matching = ProductItem.objects.annotate(
        total_variations=Count('variation'),
        matching_variations=Count('variation', filter=Q(variation__in=variations_list))
    ).filter(
        matching_variations=variations_len,
        total_variations=variations_len
    )
    
    # 🚨 product_id
    # Агрегируем суммы value по product_id и сортируем по total_value и date_added
    aggregated = Price.objects.filter(product__in=matching).values('product_id', 'product__date_added').annotate(
    # aggregated = Price.objects.filter(product__in=matching).values('product_id').annotate(
        total_value=Sum('value')
    ).order_by('total_value', 'product__date_added')

    # Находим минимальную сумму
    min_total_value = aggregated.aggregate(min_value=Min('total_value'))['min_value']

    # Находим product_id с минимальной суммой value
    min_price_product_id = aggregated.filter(total_value=min_total_value) #.first()
    print("🚨🚨🚨🚨🚨🚨🚨")
    print(min_price_product_id)
    print("🚨🚨🚨🚨🚨🚨🚨")

    return min_price_product_id.first()["product_id"]

    
def update_product_entry(instance, prices):
    instance_variation_option_id = instance.variation.get(variation=1).pk

    matrix = instance.product.data.get('sizes')
    product_item_id = get_min_price_product_item_id(instance_variation_option_id)
    variation_option = VariationOption.objects.get(product_item=product_item_id)
    if matrix:
        head = matrix[0]
        body = matrix[1]
        for index, item in enumerate(body):
            if item[0] == instance_variation_option_id:
                head[1:-1] = list(variation_option.data.keys())
                head[-1] = list(prices.values_list("currency__iso", flat=True))
                body[index] = [variation_option.id, *list(variation_option.data.values())]
                decimal_price_list = list(prices.values_list("value", flat=True))
                body[index][-1] = list(map(float, decimal_price_list))
                break
        else:
            body.append([variation_option.id, *list(variation_option.data.values())])
            decimal_price_list = list(prices.values_list("value", flat=True))
            body[-1][-1] = list(map(float, decimal_price_list))
            body = sorted(body, key=lambda x: x[0])
        matrix = [head, body]
        instance.product.data['sizes'] = matrix
        instance.product.save()
    else:
        head = ["id", *list(variation_option.data.keys())]
        head[-1] = list(prices.values_list("currency__iso", flat=True))
        body = [variation_option.id, *list(variation_option.data.values())]
        decimal_price_list = list(prices.values_list("value", flat=True))
        body[-1] = list(map(float, decimal_price_list))
        matrix = [head, [body]]
        instance.product.data['sizes'] = matrix
        instance.product.save()

    print('MATRIX')
    pprint(matrix)



@receiver(my_signal)
def my_signal_handler(sender, instance, request, variation_pk_set, prices, **kwargs):
    # ... логика обработчика ...
    if variation_pk_set:
        validate_variations(variation_pk_set)
    if prices:
        validate_prices(prices)
    update_product_entry(instance, prices)
    print(request.user)
    print(f"Сигнал получен от {sender}, ")

# @receiver(m2m_changed, sender=ProductItem.variation.through)
# def check_option_variation(sender, instance, action, pk_set, **kwargs):
#     if action == 'validate_variations':
#         new_variations = VariationOption.objects.filter(pk__in=pk_set).values_list('variation_id', flat=True)
#         if len(set(new_variations)) != len(new_variations):
#             raise ValidationError("Duplicate variation detected in Options.")
#     elif action == 'pre_add':
#         existing_variations = instance.variation.values_list('variation_id', flat=True)
#         new_variations = VariationOption.objects.filter(pk__in=pk_set).values_list('variation_id', flat=True)
#         if set(existing_variations) & set(new_variations):
#             raise ValidationError("Duplicate variation detected in Options.")