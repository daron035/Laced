import Carousel from "@/components/common/Carousel";
import Sl from "@/components/common/Sl";
import { Path, getData } from "@/components/utils";

async function getD() {
  const res = await fetch("http://django:8000/api/product/related_products/");
  // The return value is *not* serialized
  // You can return Date, Map, Set, etc.

  if (!res.ok) {
    // This will activate the closest `error.js` Error Boundary
    throw new Error("Failed to fetch data");
  }

  return res.json();
}
export default async function Page() {
  // const data = await getData("product/related_products/");
  // const data = await getD();
  const data = await getData(Path.related_products);

  // console.log("eweweewwewewe", data);
  return (
    <div className="">
      <Sl />
      {/* {data && data} */}
      <div className="max-w-[1162px] mx-auto">
        {data && <Carousel data={data} title="recently viewed" />}
        {data && <Carousel data={data} title="related products" />}
      </div>
    </div>
  );
}
