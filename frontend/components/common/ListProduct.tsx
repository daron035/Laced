"use client";

import styles from "@/styles/listProduct.module.scss";
import Image from "next/image";

interface Props {
  iteme: any;
}

export default function Page({ item }: Props) {
  console.log(item.price_from);
  return (
    <div className={styles.container__item}>
      <div className="overflow-hidden">
        <Image
          src="/new_balance_650r_white_black_1.jpg"
          width={350}
          height={350}
          alt="Picture of the author"
          className={styles.a}
        />
      </div>
      <div className="text-center mb-[15px] z-50">{item.name}</div>
      <div className="text-center pb-[60px]">
        From {item.price_from.symbol}
        {item.price_from.value}
      </div>
    </div>
  );
}
