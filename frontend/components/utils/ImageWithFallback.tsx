"use client";

import Image from "next/image";
import { getImgURL } from "@/utils/image.utils";

interface Props {
  src: string;
  width: number;
  height: number;
  alt: string;
  className: string | undefined;
}

export default function ImageWithFallback({
  src,
  width,
  height,
  alt,
  className,
}: Props) {
  const imageUrl = getImgURL(src, "300:300");

  return (
    <Image
      src={imageUrl}
      width={width}
      height={height}
      alt={alt}
      className={className}
    />
  );
}
