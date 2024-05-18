"use client";
import Image from "next/image";
import React, { useEffect, useRef, useState } from "react";
import styled, { keyframes } from "styled-components";
import styles from "../../styles/slider.module.scss";

// export default function Slider() {
//   return <div className="max-w-full h-[550px] relative"></div>;
// }

const Slide = styled.div`
  opacity: ${({ active }: any) => (active ? 1 : 0)};
  animation: ${({ active }: any) => (active ? "fadeIn" : "fadeOut")} 1.5s
    ease-in-out;
  transition: opacity 0.3s ease-in-out;
`;

const Text = styled.div`
  color: #f2f2f2;
  font-size: 15px;
  padding: 8px 12px;
  position: absolute;
  bottom: 8px;
  width: 100%;
  text-align: center;
`;

const NumText = styled.div`
  color: #f2f2f2;
  font-size: 12px;
  padding: 8px 12px;
  position: absolute;
  top: 0;
`;

const Dot = styled.span`
  height: 15px;
  width: 15px;
  margin: 0 2px;
  background-color: #bbb;
  border-radius: 50%;
  display: inline-block;
  transition: background-color 0.6s ease;
  background-color: ${({ active }: any) => (active ? "#717171" : "#bbb")};
`;

const images = ["/3bg.jpeg", "/bg.jpeg", "/bgg.jpeg"];

export default function Slider() {
  const [slideIndex, setSlideIndex] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      setSlideIndex((prevIndex) => (prevIndex + 1) % images.length);
    }, 2000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div className={styles.slideshow}>
      <div className={styles.slides}>
        {images.map((image, index) => (
          <div
            key={index}
            className={`${styles.slide} ${
              slideIndex === index
                ? "opacity-1 duration-700"
                : "opacity-0 duration-700"
            }`}
          >
            <NumText>{index + 1} / 3</NumText>
            <Image
              src={image}
              width={1920}
              height={550}
              alt={`Image ${index + 1}`}
              // style={{ width: "100%" }}
            />
            <Text>Caption Text</Text>
          </div>
        ))}
      </div>
      <br />
      <div style={{ textAlign: "center" }}>
        {images.map((_, index) => (
          <Dot key={index} active={index === slideIndex}></Dot>
        ))}
      </div>
    </div>
  );
}
