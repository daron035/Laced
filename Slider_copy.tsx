"use client";
import Image from "next/image";
import styles from "../../styles/slider.module.scss";
import { useRef, useState } from "react";
import React, { useEffect } from "react";
import styled, { keyframes } from "styled-components";

// export default function Slider() {
//   return <div className="max-w-full h-[550px] relative"></div>;
// }

const fadeOut = keyframes`
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
`;

const fadeIn = keyframes`
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
`;

const Container = styled.div`
  max-width: 100%;
`;
const SlideshowContainer = styled.div`
  position: relative;
  height: 550px;
  overflow: hidden;
  /* margin: auto; */
`;

const Slides = styled.div``;

interface StyledProp {
  readonly $isActive: boolean;
}

const Slide = styled.div<{ $isActive: boolean }>`
  position: absolute;
  opacity: ${(props) => (props.$isActive ? "1" : "0")};
  animation: ${(props) =>
    props.$isActive ? "fadeIn 1.5s ease-in-out" : "dafeOut 1.5s ease-in-out"};
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

const Dot = styled.span<StyledProp>`
  height: 15px;
  width: 15px;
  margin: 0 2px;
  background-color: #bbb;
  border-radius: 50%;
  display: inline-block;
  transition: background-color 0.6s ease;
  background-color: ${(props) => (props.$isActive ? "#717171" : "#bbb")};
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
    <Container>
      <SlideshowContainer>
        <Slides>
          {images.map((image, index) => (
            <Slide key={index} $isActive={index === slideIndex}>
              <NumText>{index + 1} / 3</NumText>
              <Image
                src={image}
                width={1920}
                height={550}
                alt={`Image ${index + 1}`}
                // style={{ width: "100%" }}
              />
              <Text>Caption Text</Text>
            </Slide>
          ))}
        </Slides>
        <br />
        <div style={{ textAlign: "center" }}>
          {images.map((_, index) => (
            <Dot key={index} $isActive={index === slideIndex}></Dot>
          ))}
        </div>
      </SlideshowContainer>
    </Container>
  );
}
