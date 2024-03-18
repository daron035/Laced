"use client";

import React, { useState } from "react";
import GeneralButton from "@/components/common/GeneralButton";
import AddToBag from "@/components/utils/AddToBag";

export default function Actions() {
  const [state, setState] = useState(0);
  const [size, setSize] = useState(0);

  const a: React.CSSProperties = {
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
            <span className="text-sm">Available Sizes:</span>
            <div className="grid grid-flow-col gap-[1px] isolate">
              {["UK", "EU", "US"].map((country, index) => {
                return (
                  <span
                    className={`flex justify-center items-center min-w-[48px] py-2 px-1 text-[12px]
                      outline cursor-pointer 
                      ${
                        index === state
                          ? "z-0 outline-2 outline-[#101010]"
                          : "outline-1 outline-[#E3E4E6]"
                      }`}
                    // onClick={() => callback('setState', index)}
                    onClick={() => setState(index)}
                  >
                    {country}
                  </span>
                );
              })}
            </div>
          </div>
          <div style={a}>
            {[1, 2, 3, 4, 5, 6, 7, 7, 7, 7, 7, 7, 7, 7].map((i, index) => {
              return (
                <span
                  className={`text-center text-[#101010] text-[12px] py-4 px-1 cursor-pointer
                    outline ${
                      index === size
                        ? "z-0 outline-2 outline-[#101010]"
                        : "outline-1 outline-[#E3E4E6] text-[#777777]"
                    }`}
                  // onClick={() => callback('setSize', index)}
                  onClick={() => setSize(index)}
                >
                  {i}
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
