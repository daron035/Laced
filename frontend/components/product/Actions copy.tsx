"use client";

import React, { useEffect, useState } from "react";
import GeneralButton from "@/components/common/GeneralButton";
import AddToBag from "@/components/utils/AddToBag";

import { Size, getCountries } from "@/utils/countries.utils";

interface StateType {
  countryIndex: number;
  selectedCountry: string;
}

export default function Actions({ data }: { data: Size[] }) {
  const [countryState, setCountryState] = useState<StateType>({
    countryIndex: 0,
    selectedCountry: "",
  });
  const [sizeState, setSizeState] = useState<{ index: number; sizeId: number }>(
    {
      index: 0,
      sizeId: 0,
    },
  );

  useEffect(() => {
    // setCountryState({
    //   ...countryState,
    //   selectedCountry: countries[countryState.countryIndex],
    // });
    setCountryState({
      ...countryState,
      selectedCountry: data[0][1],
    });
    console.log(countryState.countryIndex)
    console.log(countryState.selectedCountry)
  }, []);

  const containerStyles: React.CSSProperties = {
    display: "grid",
    rowGap: "1px",
    columnGap: "1px",
    gridAutoFlow: "unset",
    isolation: "isolate", // из-за z-index'ов
    gridTemplateColumns: "repeat(auto-fill, minmax(80px, 1fr))",
  };

  // console.log(data);
  // const countries = getCountries(data);
  // const countries = data[0].slice(1, -1);
  const countries = data[0].slice(1, -1);
  // console.log("contries", countries);

  return (
    <>
      <div>
        <div className="text-[#101010]">
          <div className="flex justify-between items-center pt-4 pb-3">
            <span className="text-sm">Available Sizes:</span>
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
                      countryIndex: index,
                      selectedCountry: countries[index],
                    })
                  }
                >
                  {country}
                </span>
              ))}
            </div>
          </div>
          {countryState.selectedCountry ? (
            <div style={containerStyles}>
              {data.map((i, index) => (
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
                      index: index,
                      sizeId: data[index]["id"],
                    })
                  }
                >
                  {i[countryState.selectedCountry]}
                </span>
              ))}
            </div>
          ) : (
            <div style={containerStyles}>
              {data.map((_, index) => (
                <span
                  key={index}
                  className={`text-center text-[#101010] text-[12px] py-4 px-1 cursor-pointer
                  outline ${
                    index === sizeState.index
                      ? "z-0 outline-2 outline-[#101010]"
                      : "outline-1 outline-[#E3E4E6] text-[#777777]"
                  }`}
                >
                  <div className="h-[13.5px]"></div>
                </span>
              ))}
            </div>
          )}
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
