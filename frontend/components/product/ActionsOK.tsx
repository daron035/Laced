"use client";

import React, { useEffect, useState } from "react";
import GeneralButton from "@/components/common/GeneralButton";
import AddToBag from "@/components/utils/AddToBag";

import { Size, getCountries } from "@/utils/countries.utils";

interface StateType {
  countryIndex: number;
  selectedCountry: string;
  j: number | null;
}

export default function Actions({ data }: { data: Size[] }) {
  const [sizeState, setSizeState] = useState<{ index: number; sizeId: number; i: any }>(
    {
      index: 0,
      sizeId: 0,
      i: 0
    },
  );
  const [countryState, setCountryState] = useState<StateType>({
    countryIndex: 0,
    selectedCountry: "",
    j: 1,
  });
  
  const countries = data[0].slice(1, -1);
  const sizes = data[1]

  useEffect(() => {
    setCountryState({
      ...countryState,
      selectedCountry: countries[0],
    });

    setSizeState({
      ...sizeState,
      sizeId: sizes[0],
    });
    
  }, []);

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
            <span className="text-sm" onClick={() => console.log(sizeState, countryState)}>Available Sizes:</span>
            <div className="grid grid-flow-col gap-[1px] isolate">
              {countries.map((country, index) => (
                <span
                  key={index}
                  className={`flex justify-center items-center min-w-[48px] py-2 px-1 text-[12px]
                    outline cursor-pointer 
                    ${
                      index === countryState.countryIndex
                        ? "z-0 outline-2 outline-[#101010]"
                        : "outline-1 outline-[#E3E4E6]"
                    }`}
                  onClick={() =>
                    setCountryState({
                      ...countryState,
                      countryIndex: index,
                      // selectedCountry: countries[index],
                      j: index+1,
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
                    index === sizeState.index
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
            {/* ${sizes[sizeState.i][3][0]} */}
            ${sizes[sizeState.i][sizes.length - 1][0]}
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
