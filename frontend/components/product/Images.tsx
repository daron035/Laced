"use client";

import Image from "next/image";
import { useState, useEffect } from "react";
import { getImgURL } from "@/utils/image.utils";

export default function Images({ images = [] }: { images: any[] }) {
  const [activeImage, setActiveImage] = useState(0);
  const [mainImage, setMainImage] = useState("");

  useEffect(() => {
    setMainImage(getImgURL(images[activeImage]?.image, "900:900"));
  }, [activeImage, images]);

  const handleImageClick = (index: number) => {
    setActiveImage(index);
  };

  return (
    <div className="flex sticky top-[72px] mt-[32px]">
      {/* Small images on the left */}
      <div className="shrink-0">
        {Object.values(images).map((image: any, index: number) => (
          <Image
            key={index}
            src={getImgURL(image?.image, "300:300")}
            width={80}
            height={80}
            alt="Picture"
            className={`cursor-pointer border-[1px] ${
              activeImage === index ? "border-[#959595]" : "border-transparent"
            }`}
            onClick={() => handleImageClick(index)}
          />
        ))}
      </div>
      {/* Main image */}
      <div className="mx-10">
        <Image src={mainImage} width={580} height={580} alt="Main Picture" />
      </div>
    </div>
  );
}
