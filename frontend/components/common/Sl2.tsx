"use client";

import Image from "next/image";
import React, { useState } from "react";
import { IoIosArrowBack, IoIosArrowForward } from "react-icons/io";

import "@/styles/head_carousel.css";

export const sliderItems = [
  {
    id: 1,
    image: "/bg.jpeg",
    title: "SUMMER ",
    // css: "absolute top-20 left-10 text-[#101010]",
    css: "",
  },
  {
    id: 2,
    image: "/bgg.jpeg",
    title: "SUMMER 2222",
    // css: "absolute top-20 left-10 text-[#101010]",
    css: "",
    e: "hidden",
  },
  {
    id: 3,
    image: "/3bg.jpeg",
    title: "SUMMER 3333",
    // css: "absolute top-20 left-10 text-[#101010]",
    css: "",
    e: "hidden",
  },
];

export default function Sl() {
  const [currentIndex, setCurrentIndex] = useState(0);

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

  const slider_container = {
    position: "relative",
    width: "100%",
    height: "100%",
  };

  const slide = {
    // position: "absolute",
    // top: "0",
    // left: "0",
    // width: "100",
    // height: "100",
    // opacity: "0",
    // transition: "opacity 0.5s ease-in-out",
    opacity: "0",
    transition: "opacity 0.5s ease-in-out",
  };

  const slide_active = {
    opacity: 1,
  };

  // <img className="" src="/3bg.jpeg" alt="asd" />
  // <div key={index} className={`width-full ${item.e}`}>
  return (
    // <div className="relative w-full h-full flex items-center max-w-[2200px] max-h-[550px] mx-auto overflow-hidden">
    <div className="carousel">
      <div className="carousel_wrapper">
        {sliderItems.map((item, index) => (
          // <div key={index} className={`width-full ${item.e}`}>
          <div
            key={index}
            // className={
            //   index === currentIndex
            //     ? `${styles.carousel_card} ${styles.carousel_card_active}`
            //     : styles.carousel_card
            // }
            className={
              index === currentIndex
                ? "carousel_card carousel_card-active"
                : "carousel_card"
            }
            // className={`width-full h-full overflow-hidden transition-opacity duration-700 ease-in-out ${index === currentIndex ? "" : "hidden"}`}
            // className={`width-full transition-opacity duration-700 ease-in-out ${index === currentIndex ? "opacity-100" : "opacity-0"}`}
            // className={`width-full ${index === currentIndex ? "opacity-1 duration-300 ease-in-out" : "hidden opacity-0 duration-300 ease-in-out"}`}
          >
            {/* <div className={item.css}> */}
            {/*   <h1 className="text-3xl">{item.title}</h1> */}
            {/*   <p>description</p> */}
            {/*   <div */}
            {/*     className="py-4 px-8 bg-[#101010] text-gray-100 rounded-lg cursor-pointer" */}
            {/*     onClick={() => console.log("sadfsdf")} */}
            {/*   > */}
            {/*     Shop */}
            {/*   </div> */}
            {/* </div> */}
            <Image
              src={sliderItems[currentIndex].image}
              // src={item.image}
              width={2200}
              height={550}
              alt="asd"
              // style={imageStyle}
              className=""
            />
          </div>
        ))}
        {/* <div className="absolute bottom-0 pb-6 pl-16 text-black flex items-center"> */}
        {/*   <IoIosArrowBack */}
        {/*     size={20} */}
        {/*     style={{ color: "#101010" }} */}
        {/*     className="cursor-pointer" */}
        {/*     onClick={goToPrevious} */}
        {/*   /> */}
        {/*   <span>{currentIndex + 1} / 3</span> */}
        {/*   <IoIosArrowForward */}
        {/*     size={20} */}
        {/*     style={{ color: "#101010" }} */}
        {/*     className="cursor-pointer" */}
        {/*     onClick={goToNext} */}
        {/*   /> */}
        {/* </div> */}
      </div>
    </div>
  );
}
