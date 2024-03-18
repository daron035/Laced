"use client";

import Image from "next/image";
import { useRef } from "react";
import { IoChevronBackOutline, IoChevronForwardOutline } from "react-icons/io5";
import styles from "../../styles/carousel.module.scss";

import { getImgURL } from "@/utils/image.utils";

interface Props {
  data: any;
  title: string | null;
}

export default function Carousel({ data, title }: Props) {
  const containerRef = useRef<HTMLDivElement>(null);
  // const itemWidth = 224; // Ширина каждого элемента
  const itemWidth = 284; // Ширина каждого элемента
  const itemsPerScroll = 5; // Количество элементов для прокрутки

  const handleNextClick = () => {
    if (containerRef.current) {
      const container = containerRef.current;
      const scrollAmount = itemWidth * itemsPerScroll;

      if (
        container.scrollLeft + container.clientWidth ===
        container.scrollWidth
      ) {
        container.scrollTo({
          left: 0,
          behavior: "smooth",
        });
      } else {
        container.scrollBy({
          left: scrollAmount,
          behavior: "smooth",
        });
      }
    }
  };

  const handlePrevClick = () => {
    if (containerRef.current) {
      const container = containerRef.current;
      const scrollAmount = itemWidth * itemsPerScroll;

      if (container.scrollLeft === 0) {
        container.scrollTo({
          left: container.scrollWidth,
          behavior: "smooth",
        });
      } else {
        container.scrollBy({
          left: -scrollAmount,
          behavior: "smooth",
        });
      }
    }
  };

  // Создаем массив с 20 элементами
  const test_items = Array.from({ length: 20 }, (_, index) => (
    <article key={index} className={`${styles.item} group cursor-pointer`}>
      <div className="w-56 h-56 mb-2 overflow-hidden">
        <div className="group-hover:scale-105 duration-500 select-none">
          <Image
            src="/new_balance_650r_white_black_1.jpg"
            width={224}
            height={224}
            alt="Picture of the author"
          />
        </div>
      </div>
      <footer className="flex flex-col gap-y-1 px-4 pb-4">
        <span>Nike</span>
        <span className="text-[#777777]">{`Item ${index + 1}`}</span>
        <span>$ 99</span>
      </footer>
    </article>
  ));

  const items = Array.from({ length: data.length }, (_, index) => {
    const prod = data[index];
    const imageUrl = getImgURL(prod.image);
    console.log("1111111111111111111111");
    console.log(prod.image);
    console.log("8888888888888888888888");
    console.log(imageUrl);

    // <Image
    //   src={imageUrl}
    //   width={224}
    //   height={224}
    //   alt="Picture of the author"
    // />
    return (
      <article key={index} className={`${styles.item} group cursor-pointer`}>
        <div className="w-56 h-56 mb-2 overflow-hidden">
          <div className="group-hover:scale-105 duration-500 select-none">
            {imageUrl && (
              <img
                src={imageUrl}
                width="224"
                height="224"
                alt="Picture of the author"
              />
            )}
          </div>
        </div>
        <footer className="flex flex-col gap-y-1 px-4 pb-4">
          <span>{prod.name}</span>
          <span className="text-[#777777]">{`Item ${prod.id}`}</span>
          <span>$ 99</span>
        </footer>
      </article>
    );
  });

  return (
    <div className="text-[#101010] pt-16">
      <div className="flex justify-between items-center mb-4">
        <div className="text-lg uppercase leading-none">{title}</div>
        <div className="flex gap-2">
          <IoChevronBackOutline
            size={28}
            style={{ color: "#101010" }}
            onClick={handlePrevClick}
            className="cursor-pointer"
          />
          <IoChevronForwardOutline
            size={28}
            style={{ color: "#101010" }}
            onClick={handleNextClick}
            className="cursor-pointer"
          />
        </div>
      </div>
      <div>
        <div className={styles.scroll_container} ref={containerRef}>
          {items}
        </div>
      </div>
    </div>
  );
}
