"use client";

import Header from "@/components/account/Header";
import Image from "next/image";
import { useEffect } from "react";
import GeneralButton from "@/components/common/GeneralButton";
import { useState } from "react";

import { useAppDispatch, useAppSelector } from "@/redux/hooks";
import { fetchCart, removeFromCart } from "@/redux/features/cartSlice";
import ImageWithFallback from "@/components/utils/ImageWithFallback";

export default function Page() {
  const dispatch = useAppDispatch();
  const cart = useAppSelector((state) => state.cart);
  const { items, currency, subtotal, status, count } = cart;
  console.log(count);

  useEffect(() => {
    dispatch(fetchCart());
  }, [dispatch]);

  const [listing, setListing] = useState({
    handling_fee: null,
    payment_fee: null,
    shipping_fee: null,
    gross_payout: null,
  });

  const handleClickCheckout = () => {
    console.log(items);
  };

  const handleClickRemove = (
    product_id: number,
    variation_id: number,
    price: any,
  ) => {
    console.log(product_id, variation_id);
    // console.log(+product_id);
    // console.log(variation_id);
    // dispatch(removeFromCart());
    dispatch(
      removeFromCart({
        product_id: product_id,
        variation_id: variation_id,
        price: price,
      }),
    );
  };

  return (
    <div className="max-w-3xl mx-auto py-12 px-10">
      <Header button={false} title="Your Bag Summary" breadCrum="Home" />
      <div className="p-10 text-gray-950 bg-white text-sm">
        {status === "succeeded" ? (
          <>
            {items && (
              <>
                {items.map((item) => (
                  <div key={item.id} className="mb-6 flex">
                    <ImageWithFallback
                      src={item.image}
                      width={80}
                      height={80}
                      alt=""
                      className="mr-4"
                    />
                    <div className="flex-1">
                      <div className="mb-1">{item.name}</div>
                      <div className="text-[#656667] text-xs">
                        {item.variation}
                      </div>
                      <div className="mt-4">
                        <span
                          className="text-xs inline border-b border-gray-950 cursor-pointer"
                          onClick={
                            () =>
                              handleClickRemove(
                                +item.product_id,
                                item.variation_id,
                                item.price.value,
                              )
                            // handleClickRemove(+item.product_id, item.variation_id)
                          }
                        >
                          Remove
                        </span>
                      </div>
                    </div>
                    <div>
                      {item.price.symbol}
                      {item.price.value}
                    </div>
                  </div>
                ))}
                <div className="py-6 text-right">
                  Subtotal: {subtotal}
                  {currency}
                </div>
                <GeneralButton
                  lg
                  action="black"
                  title="Checkout"
                  onClick={handleClickCheckout}
                />
              </>
            )}
          </>
        ) : (
          <div className="text-xl text-center">🛒 is empty 😔</div>
        )}
      </div>
    </div>
  );
}
