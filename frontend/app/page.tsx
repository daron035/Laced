"use server"

import Carousel from "@/components/common/Carousel";
import Sl from "@/components/common/Sl";
import { headers } from "next/headers";
import { getData } from "@/utils/car";


export default async function Page() {
  const data = await getData("related_products");
  const ip = headers().get("x-forwarded-for");

  return (
    <div className="">
      <Sl />
      <p>
          IP Address:
          {` ${ip}` || " Not found"}
        </p>
      <div className="max-w-[1162px] mx-auto">
        {data && <Carousel data={data} title="related products" />}
      </div>
    </div>
  );
}
