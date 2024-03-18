"use client";

import Header from "@/components/account/Header";
import GeneralButton from "@/components/common/GeneralButton";
import { Search } from "@/components/common/svgs";
import Images from "@/components/product/Images";
import { IoAddOutline, IoRemoveOutline } from "react-icons/io5";
import Image from "next/image";
import { useEffect, useState, MouseEventHandler } from "react";

interface ListingState {
  handling_fee: number;
  payment_fee: number;
  shipping_fee: number;
  gross_payout: number;
  price: number;
  // handling_fee: number | null;
  // payment_fee: number | null;
  // shipping_fee: number | null;
  // gross_payout: number | null;
  // price: number | null;
}

export default function Page() {
  const defaultPrice = 65;
  const defaultShippingPrice = 6.99;

  const formatNumber = (num: number) => num.toFixed(2);

  const calculateListing = (newPrice: number, shipingPrice: number) => {
    const handling_fee = parseFloat((newPrice * 0.12).toFixed(2));
    const payment_fee = parseFloat((newPrice * 0.03).toFixed(2));
    const gross_payout = parseFloat(
      (newPrice - (handling_fee + payment_fee + shipingPrice)).toFixed(2),
    );

    return {
      price: newPrice,
      handling_fee,
      payment_fee,
      shipping_fee: shipingPrice,
      gross_payout,
    };
  };

  const [listing, setListing] = useState<ListingState>(
    calculateListing(defaultPrice, defaultShippingPrice),
  );

  const updateListing = (newPrice: number, shipingPrice: number) => {
    setListing(calculateListing(newPrice, shipingPrice));
  };

  const adjustPrice = (amount: number) => {
    const newPrice = listing.price + amount;
    updateListing(newPrice, listing.shipping_fee);
  };

  // const decrement = (event: MouseEvent) => {
  const decrement = (event: React.MouseEvent<HTMLButtonElement>) => {
    event.preventDefault();
    adjustPrice(-5);
  };

  // const increment = (event: MouseEvent) => {
  const increment = (event: React.MouseEvent<HTMLButtonElement>) => {
    event.preventDefault();
    adjustPrice(5);
  };

  useEffect(() => {
    updateListing(defaultPrice, defaultShippingPrice);
  }, [defaultPrice]);
  return (
    <>
      <Header button={false} title="Sell Items" breadCrum="Back" />
      <div className="bg-white">
        <div className="py-6 px-10 flex text-gray-950">
          <Image
            src="/new_balance_650r_white_black_1.jpg"
            width={128}
            height={128}
            alt=""
            className="mr-4"
          />
          <div className="flex flex-col justify-center">
            <p className="text-sm">Yeezy Slide Slate Grey</p>
            <div className="text-xs text-gray-500">2023 | ID2350</div>
          </div>
        </div>
        <form action="" className="text-gray-950">
          <div className="p-10">
            <h5 className="uppercase mb-6 text-sm">Listing Details</h5>
            <div className="mb-6">
              <label
                htmlFor="size"
                className="block text-xs mb-1 text-gray-500"
              >
                Size
              </label>
              <select
                name="size"
                id="size"
                className="w-full p-4 pr-11 outline-none appearance-none border border-gray-400 rounded"
              >
                <option value="petersburg">Санкт-Петербург</option>
                <option value="samara">Самара</option>
                <option value="perm">Пермь</option>
                <option value="novosibirsk">Новосибирск</option>
              </select>
            </div>
            <div className="">
              <label
                htmlFor="quantity"
                className="block text-xs mb-1 text-gray-500"
              >
                Quantity
              </label>
              <select
                name="quantity"
                id="quantity"
                className="w-full p-4 pr-11 outline-none appearance-none border border-gray-400 rounded"
              >
                <option value="petersburg">1</option>
                <option value="samara">Самара</option>
                <option value="perm">Пермь</option>
                <option value="novosibirsk">Новосибирск</option>
              </select>
            </div>
          </div>
          <div className="pt-10 px-10 text-gray-950">
            <h5 className="uppercase mb-6 text-sm">Listing Price</h5>
            <div className="flex items-center">
              <div className="flex flex-1">
                <div>
                  <sup className="top-1">$</sup>
                </div>
                <span className="text-5xl ml-1">{listing.price}</span>
              </div>
              <button
                className="border rounded border-gray-400 h-8 w-8 flex justify-center items-center"
                // onClick={(e) => decrement(e, "323232323")}
                onClick={(e) => decrement(e)}
              >
                <IoRemoveOutline size={16} />
              </button>
              <button
                className="border rounded border-gray-400 h-8 w-8 flex justify-center items-center ml-1"
                onClick={(e) => increment(e)}
              >
                <IoAddOutline size={16} />
              </button>
            </div>
          </div>
          <div className="p-10 text-gray-500">
            <table className="mb-6 w-full border border-separate rounded text-sm">
              <tbody className="divide-y">
                <tr className="flex justify-between">
                  <td className="p-4">Handling Fee (12%)</td>
                  <td className="p-4">
                    -${formatNumber(listing.handling_fee)}
                  </td>
                </tr>
                <tr className="flex justify-between">
                  <td className="p-4">Payment Fee (3%)</td>
                  <td className="p-4">-${formatNumber(listing.payment_fee)}</td>
                </tr>
                <tr className="flex justify-between">
                  <td className="p-4">Shipping Fee</td>
                  <td className="p-4">
                    -${formatNumber(listing.shipping_fee)}
                  </td>
                </tr>
                <tr className="flex justify-between text-gray-950">
                  <td className="p-4">Gross Payout</td>
                  <td className="p-4">${formatNumber(listing.gross_payout)}</td>
                </tr>
              </tbody>
            </table>
            <p className="mt-2 text-xs text-gray-950">
              There will be at least 3 products ahead of you in the queue. Beat
              the lowest price of £70 to be first in the queue.
            </p>
            <div className="mt-8 flex gap-x-6">
              <GeneralButton
                sm
                action="white"
                title="Cancel"
                style={{
                  width: "150px",
                  marginLeft: "auto",
                  border: "none",
                  textDecoration: "underline",
                }}
              />
              <GeneralButton
                lg
                action="black"
                title="Done"
                style={{ width: "300px" }}
              />
            </div>
          </div>
        </form>
      </div>
    </>
  );
}
