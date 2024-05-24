"use client";

import { useRouter, useSearchParams } from "next/navigation";
import GeneralButton from "@/components/common/GeneralButton";
// import { addItemToCart } from "@/redux/features/cartSlice";
import { useAppDispatch } from "@/redux/hooks";
import React, { useState } from "react";

import { getPrice, getMinPrice } from "@/utils/price.utils";
import { getCookie } from "@/utils";

declare global {
  interface Window {
    YooMoneyCheckout: any;
  }
}

interface StateType {
  countryCursor: number;
  sizeIndex: number;
}

function NoDataAvailable() {
  return (
    <>
      <div className="flex justify-between items-center pt-4 pb-3">
        <span className="text-sm">Available Sizes: No available sizes</span>
      </div>
      <GeneralButton lg action="white" title="sell this item" />
    </>
  );
}

export default function Actions({
  data_matrix,
  product_id,
  currency_iso,
  currency_symbol,
}: {
  data_matrix: any[];
  product_id: number;
  currency_iso: string;
  currency_symbol: string;
}) {
  const dispatch = useAppDispatch();

  // Получаем списки стран и размеров из переданных данных
  // console.log(data_matrix);
  const countries = data_matrix[0].slice(1, -1); // ["id"，"UK", "EU", ["GBR", "EUR"]]
  const allSizes = data_matrix[1]; //               [[33, 3, 36, [22, 130, 160]],
  //                                                 [41, 4, 37, [23, 140, 180]]]
  const minPriceID = getMinPrice(allSizes);
  const [state, setState] = useState<StateType>({
    sizeIndex: minPriceID || 0, //     i
    countryCursor: 0, // j
  });
  const selectedSize = allSizes[state.sizeIndex]; // [33, 3, 36, [130, 160]]
  const currencies: string[] = data_matrix[0][data_matrix[0].length - 1]; // ["GBR", "EUR"]
  const currencyID = currencies.indexOf(currency_iso);

  const handleCountryClick = (index: number) => {
    setState((prevState) => ({
      ...prevState,
      countryCursor: index,
    }));
  };

  const handleSizeClick = (index: number) => {
    setState((prevState) => ({
      ...prevState,
      sizeIndex: index,
    }));
  };

  const handlePayment = async () => {
    // const checkout = new window.YooMoneyCheckout(983923);
    const checkout = new window.YooMoneyCheckout(391979);
    let response: any;
    await checkout
      .tokenize({
        number: "4111111111111111",
        cvc: "234",
        month: "11",
        year: "25",
      })
      .then((res: any) => {
        if (res.status === "success") {
          // if (res.status === "200") {

          // const { paymentToken } = res.data.response;
          // response = paymentToken;
          response = res.data.response.paymentToken;
          console.log(response);

          // setPaymentToken(res.data.response);
        } else {
          response = res;
          console.log("YooKassa FAILED");
        }
      })
      .catch((error: any) => {
        console.error("Ошибка при токенизации:", error);
      });
    return response;
    console.log("390239239023923");
    // dispatch(addItemToCart(id));
    // window.location.href = "/cart";
  };

  const router = useRouter();
  const handleClickAddToBagButton = async () => {
    // router.push("http://127.0.0.1:3000/products");
    try {
      const token = await handlePayment();
      const amount = 301;
      console.log("final", token);

      // Отправка токена на бэкенд Django
      const response = await fetch(
        `${process.env.NEXT_PUBLIC_HOST}/api/payment/`,
        {
          method: "POST",
          cache: "no-store",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ token, amount }),
        },
      );
      let result = await response.json();
      console.log("32323233223", result);
      console.log("HTTP статус ответа:", response.status);
      router.push(".");
      if (response.status === 202) {
        // Токен успешно отправлен на бэкенд Django
        console.log("Токен успешно отправлен на бэкенд Django!");
        // Можете выполнять дополнительные действия здесь при необходимости
      } else {
        // Ошибка при отправке токена на бэкенд
        console.error("Не удалось отправить токен на бэкенд Django.");
      }
    } catch (err) {
      console.error("Ошибка при обработке оплаты:", err);
    }
  };

  if (!data_matrix || data_matrix.length === 0) {
    return <NoDataAvailable />;
  }

  return (
    <>
      <div>
        <div className="text-[#101010]">
          <div className="flex justify-between items-center pt-4 pb-3">
            <span className="text-sm">Available Sizes:</span>
            <div className="grid grid-flow-col gap-[1px] isolate">
              {countries.map((country: string, index: number) => (
                <span
                  key={index}
                  className={`flex justify-center items-center min-w-[48px] py-2 px-1 text-[12px]
                    outline cursor-pointer uppercase
                    ${
                      index === state.countryCursor
                        ? "z-0 outline-2 outline-[#101010]"
                        : "outline-1 outline-[#E3E4E6]"
                    }`}
                  onClick={() => handleCountryClick(index)}
                >
                  {country}
                </span>
              ))}
            </div>
          </div>
          <div
            style={{
              display: "grid",
              rowGap: "1px",
              columnGap: "1px",
              gridAutoFlow: "unset",
              isolation: "isolate",
              gridTemplateColumns: "repeat(auto-fill, minmax(80px, 1fr))",
            }}
          >
            {allSizes.map((item: number[], index: number) => (
              <span
                key={index}
                className={`text-center text-[#101010] text-[12px] py-4 px-1 cursor-pointer
                  outline ${
                    index === state.sizeIndex
                      ? "z-0 outline-2 outline-[#101010]"
                      : "outline-1 outline-[#E3E4E6] text-[#777777]"
                  }`}
                onClick={() => handleSizeClick(index)}
              >
                {item[state.countryCursor + 1]}
              </span>
            ))}
          </div>
        </div>
        <div className="text-[#101010] text-3xl mt-8 subpixel-antialiased">
          {currency_symbol}
          {selectedSize[selectedSize.length - 1][currencyID]}
        </div>
      </div>
      <div className="mt-8 pb-12 space-y-6">
        <GeneralButton
          lg
          action="black"
          title="add to bag"
          onClick={() => handleClickAddToBagButton()}
        />
        <GeneralButton lg action="white" title="sell this item" />
      </div>
    </>
  );
}
