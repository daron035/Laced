"use client";

import { useRef } from "react";
import { IoChevronBackOutline, IoChevronForwardOutline } from "react-icons/io5";
import styles from "../../styles/carousel.module.scss";
import { getImgURL } from "@/utils/image.utils";
import Link from "next/link";
import ImageWithFallback from "@/components/utils/ImageWithFallback";
import { getCookie, setCookie, deleteCookie } from "@/utils";

interface Product {
  id: number;
  brand: string;
  name: string;
  image: string;
  slug: string;
  price_from: {
    symbol: string;
    currency: string;
    value: string;
  };
}

interface Props {
  data?: Product[];
  title?:
    | "related products"
    | "recently viewed"
    | "trending now"
    | "new arrivals";
}

function ProductCard({ product }: { product: Product }) {
  const imageUrl = getImgURL(product.image, "300:300");

  const a = getCookie("currency");

  const priceValue = product.price_from.value;
  console.log("qqq", product);
  const formattedPrice = priceValue
    ? Number.isInteger(parseFloat(priceValue))
      ? product.price_from.symbol + parseFloat(priceValue).toFixed(0)
      : product.price_from.symbol + parseFloat(priceValue).toFixed(2)
    : "";

  return (
    <Link href={`/products/${product.slug}`}>
      <article className={`${styles.item} group cursor-pointer`}>
        <div className="w-56 h-56 mb-2 overflow-hidden">
          <div className="group-hover:scale-105 duration-500 select-none">
            <ImageWithFallback
              src={product.image}
              width={224}
              height={224}
              alt="Product"
            />
          </div>
        </div>
        <footer className="flex flex-col gap-y-1 px-4 pb-4">
          <span>{product.name}</span>
          <span className="text-[#777777]">{product.brand}</span>
          <span>{formattedPrice}</span>
        </footer>
      </article>
    </Link>
  );
}

export default function Carousel({ data: propData, title }: Props) {
  console.log("propData", propData);
  const containerRef = useRef<HTMLDivElement>(null);
  const itemWidth = 284;
  const itemsPerScroll = 4;

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
      <div className={styles.scroll_container} ref={containerRef}>
        {propData?.map((product: Product, index: number) => (
          <ProductCard key={index} product={product} />
        ))}
      </div>
    </div>
  );
}
