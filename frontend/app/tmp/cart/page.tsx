"use client";

import Header from "@/components/account/Header";
import Image from "next/image";
import GeneralButton from "@/components/common/GeneralButton";
import { useState } from "react";

export default function Page() {
  const [listing, setListing] = useState({
    handling_fee: null,
    payment_fee: null,
    shipping_fee: null,
    gross_payout: null,
  });

  return (
    <div className="max-w-3xl mx-auto py-12 px-10">
      <Header button={false} title="Your Bag Summary" breadCrum="Home" />
      <div className="p-10 text-gray-950 bg-white">
        <div className="text-sm">
          <div className="mb-6 flex items-center">
            <Image
              src="/new_balance_650r_white_black_1.jpg"
              width={80}
              height={80}
              alt=""
              className="mr-4"
            />
            <div>
              <div>Yeezy Slide Slate Grey</div>
              <div className="text-[#656667]">2023 | ID2350</div>
              <div className="mt-4">
                <span className="text-xs inline border-b border-gray-950 cursor-pointer">
                  Remove
                </span>
              </div>
            </div>
          </div>

          <div className="mb-6 flex items-center">
            <Image
              src="/new_balance_650r_white_black_1.jpg"
              width={80}
              height={80}
              alt=""
              className="mr-4"
            />
            <div>
              <div>Yeezy Slide Slate Grey</div>
              <div className="text-[#656667]">2023 | ID2350</div>
              <div className="mt-4">
                <span className="text-xs inline border-b border-gray-950 cursor-pointer">
                  Remove
                </span>
              </div>
            </div>
          </div>
        </div>
        <div className="py-6 text-right">Subtotal: 190$</div>
        <GeneralButton lg action="black" title="Checkout" />
      </div>
    </div>
  );
}
