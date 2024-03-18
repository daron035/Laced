import re


def replace_comma_and_dash(input_string):
    # Replace comma with dot
    result_string = re.sub(r",", ".", input_string)

    # Replace any other dash with regular dash
    # result_string = re.sub(r"[-‐‑‒–—―]", "-", result_string)
    result_string = re.sub(
        r"[-\u002D\u2010\u2011\u2012\u2013\u2014\u2015]", "-", result_string
    )

    return result_string


# Example usage
# input_text = "0,5–3\u2013ЛТ"
# input_text = "0,5–3—ЛТ"
input_text = "0,5–3—лТ-H9-01"
# input_text = "0-5–3—ЛТ-H9-01"
# input_text = "1-3-ЛТ"
# input_text= "0,5–3-ЛТ"  # Пример строки с различными видами тире
# input_text = "This, is a - sample—text with various dashes"
output_text = replace_comma_and_dash(input_text)

print("Original text:", input_text)
print("Modified text:", output_text)


print(output_text.split("-", 3))
