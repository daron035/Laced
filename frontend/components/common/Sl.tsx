"use client";
import Image from "next/image";
import React, { useState } from "react";
import { IoIosArrowBack, IoIosArrowForward } from "react-icons/io";

export const sliderItems = [
  {
    id: 1,
    image: "/bg.jpeg",
    title: "SUMMER ",
    css: "absolute top-20 left-10 text-[#101010]",
  },
  {
    id: 2,
    image: "/bgg.jpeg",
    title: "SUMMER 2222",
    css: "absolute top-20 left-10 text-[#101010]",
    e: "hidden",
  },
  {
    id: 3,
    image: "/3bg.jpeg",
    title: "SUMMER 3333",
    css: "absolute top-20 left-10 text-[#101010]",
    e: "hidden",
  },
];

export default function Sl() {
  const [currentIndex, setCurrentIndex] = useState(2);

  const goToPrevious = () => {
    const isFirstSlide = currentIndex === 0;
    const newIndex = isFirstSlide ? sliderItems.length - 1 : currentIndex - 1;
    setCurrentIndex(newIndex);
  };

  const goToNext = () => {
    const isLastSlide = currentIndex === sliderItems.length - 1;
    const newIndex = isLastSlide ? 0 : currentIndex + 1;
    setCurrentIndex(newIndex);
  };

  const imageStyle = {
    border: "1px solid #fff",
  };

  // <img className="" src="/3bg.jpeg" alt="asd" />
  return (
    <div className="flex items-center relative max-w-[2200px] max-h-[550px] mx-auto overflow-hidden">
      {sliderItems.map((item, index) => (
        <div key={index} className={`width-full ${item.e}`}>
          <div className={item.css}>
            <h1 className="text-3xl">{item.title}</h1>
            <p>description</p>
            <div
              className="py-4 px-8 bg-[#101010] text-gray-100 rounded-lg cursor-pointer"
              onClick={() => console.log("sadfsdf")}
            >
              Shop
            </div>
          </div>
          <Image
            src={item.image}
            width={2200}
            height={550}
            alt="asd"
            style={imageStyle}
            className=""
          />
        </div>
      ))}
      <div className="absolute bottom-0 pb-6 pl-16 text-red-700 flex items-center">
        <IoIosArrowBack
          size={28}
          style={{ color: "#101010" }}
          className="cursor-pointer"
        />
        <span>1 / 3</span>
        <IoIosArrowForward
          size={28}
          style={{ color: "#101010" }}
          className="cursor-pointer"
        />
      </div>
    </div>
  );
}
