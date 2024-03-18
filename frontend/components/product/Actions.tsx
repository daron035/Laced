"use client";

import React, { useEffect, useState } from "react";
import GeneralButton from "@/components/common/GeneralButton";
import AddToBag from "@/components/utils/AddToBag";
import { Size, getCountries } from "@/utils/countries.utils";

interface StateType {
  countryCursor: number;
  j: number | null;
}

// data: [
//   ['id', 'UK', 'EU', ["GBP", "EUR"]],
//   [
//     [33, 3.3, 36, [130, 160]],
//     [41, 4.0, 37, [140, 180]]
//   ]
// ]

const a = { UK: 1 };
console.log(a);
export default function Actions({ data }: { data: Size[] }) {
  const [sizeState, setSizeState] = useState<{ i: any }>({
    i: 0,
  });
  const [countryState, setCountryState] = useState<StateType>({
    j: 1,
    countryCursor: 0,
  });

  // Получаем списки стран и размеров из переданных данных
  const countries = data[0].slice(1, -1); // ['UK', 'EU']
  const sizes = data[1];
  const price = sizes[sizeState.i].slice(-1)[0][0]; // slice(-1)[0] это последний элемент списка

  // Стили для контейнера размеров
  const containerStyles: React.CSSProperties = {
    display: "grid",
    rowGap: "1px",
    columnGap: "1px",
    gridAutoFlow: "unset",
    isolation: "isolate", // из-за z-index'ов
    gridTemplateColumns: "repeat(auto-fill, minmax(80px, 1fr))",
  };

  return (
    <>
      <div>
        <div className="text-[#101010]">
          <div className="flex justify-between items-center pt-4 pb-3">
            <span
              className="text-sm"
              onClick={() => console.log(sizeState, countryState)}
            >
              Available Sizes:
            </span>
            <div className="grid grid-flow-col gap-[1px] isolate">
              {countries.map((country, index) => (
                <span
                  key={index}
                  className={`flex justify-center items-center min-w-[48px] py-2 px-1 text-[12px]
                    outline cursor-pointer 
                    ${
                      index === countryState.countryCursor
                        ? "z-0 outline-2 outline-[#101010]"
                        : "outline-1 outline-[#E3E4E6]"
                    }`}
                  onClick={() =>
                    setCountryState({
                      ...countryState,
                      countryCursor: index,
                      j: index + 1,
                    })
                  }
                >
                  {country}
                </span>
              ))}
            </div>
          </div>
          <div style={containerStyles}>
            {sizes.map((item, index) => (
              <span
                key={index}
                className={`text-center text-[#101010] text-[12px] py-4 px-1 cursor-pointer
                  outline ${
                    index === sizeState.i
                      ? "z-0 outline-2 outline-[#101010]"
                      : "outline-1 outline-[#E3E4E6] text-[#777777]"
                  }`}
                onClick={() =>
                  setSizeState({
                    ...sizeState,
                    index: index,
                    i: index,
                  })
                }
              >
                {item[countryState.j]}
              </span>
            ))}
          </div>
        </div>
        <div className="text-[#101010] text-3xl mt-8 subpixel-antialiased">
          ${price}
        </div>
      </div>
      <div className="mt-8 pb-12 space-y-6">
        <GeneralButton
          lg
          action="black"
          title="add to bag"
          onClick={AddToBag}
        />
        <GeneralButton lg action="white" title="sell this item" />
      </div>
    </>
  );
}
