"use client";

import Image from "next/image";
import { ChangeEvent, FormEvent, useState } from "react";

const count = [1, 2, 3, 4];

interface SizeData {
  UK: number;
  EU: number;
  US: number;
}

const jsonData = {
  sizes: [
    { UK: 25, EU: 35, US: 3 },
    { UK: 2, EU: 3, US: 4 },
  ],
};

export default function Images() {
  const [activeImage, setActiveImage] = useState(0);

  return (
    <div className="flex sticky top-[72px] mt-[32px]">
      {/* маленькие картики слева */}
      <div className="shrink-0">
        {count.map((img, index) => {
          return (
            <Image
              src="/new_balance_650r_white_black_1.jpg"
              width={80}
              height={80}
              alt="Picture of the author"
              className={`cursor-pointer border-[1px] border-transparent${
                activeImage === index ? "border-[1px] border-[#959595]" : ""
              }`}
              onClick={() => setActiveImage(index)}
            />
          );
        })}
      </div>
      {/* main image */}
      <div className="mx-10">
        <Image
          src="/new_balance_650r_white_black_1.jpg"
          width={580}
          height={580}
          alt="Picture of the author"
        />
      </div>
    </div>
  );
}
