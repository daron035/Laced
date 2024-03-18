"use client";

import React, { useEffect, useState } from "react";
import GeneralButton from "@/components/common/GeneralButton";
import AddToBag from "@/components/utils/AddToBag";

import { getCountries } from "@/utils/countries.utils";

export default function Actions() {
  const [state, setState] = useState({ index: 0, countryA2: null });
  const [size, setSize] = useState(0);

  useEffect(() => {
    setState({ ...state, countryA2: countries[state.index] });
  }, []);

  console.log(state);
  console.log(size);
  const a: React.CSSProperties = {
    display: "grid",
    rowGap: "1px",
    columnGap: "1px",
    gridAutoFlow: "unset",
    isolation: "isolate", // из-за z-index'ов
    gridTemplateColumns: "repeat(auto-fill, minmax(80px, 1fr))",
  };

  const jsData: JsData = {
    sizes: [
      { id: 3, UK: 3, EU: 36, price: { GBP: 130, EUR: 150 } },
      { id: 4, UK: 4, EU: 37, price: { GBP: 140, EUR: 160 } },
      { id: 5, UK: 5, EU: 38, price: { GBP: 150, EUR: 180 } },
    ],
    description: {
      ru: "фывафоыва",
      eu: "asdfasfas",
    },
  };

  const countries = getCountries(jsData);

  // console.log(countries[0]);

  return (
    <>
      <div>
        <div className="text-[#101010]">
          <div className="flex justify-between items-center pt-4 pb-3">
            <span className="text-sm">Available Sizes:</span>
            <div className="grid grid-flow-col gap-[1px] isolate">
              {countries.map((country, index) => {
                return (
                  <span
                    className={`flex justify-center items-center min-w-[48px] py-2 px-1 text-[12px]
                      outline cursor-pointer 
                      ${
                        index === state.index
                          ? "z-0 outline-2 outline-[#101010]"
                          : "outline-1 outline-[#E3E4E6]"
                      }`}
                    onClick={(e) =>
                      setState({ index: index, countryA2: countries[index] })
                    }
                  >
                    {country}
                  </span>
                );
              })}
            </div>
          </div>
          <div style={a}>
            {jsData.sizes.map((i, index) => {
              return (
                <span
                  className={`text-center text-[#101010] text-[12px] py-4 px-1 cursor-pointer
                    outline ${
                      index === size
                        ? "z-0 outline-2 outline-[#101010]"
                        : "outline-1 outline-[#E3E4E6] text-[#777777]"
                    }`}
                  onClick={() => setSize(index)}
                >
                  {i[state.countryA2]}
                </span>
              );
            })}
          </div>
        </div>
        <div className="text-[#101010] text-3xl mt-8 subpixel-antialiased">
          $230
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
