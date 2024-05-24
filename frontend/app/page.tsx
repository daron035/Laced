import Carousel from "@/components/common/Carousel";
import Sl from "@/components/common/Sl";
import { Path, getData } from "@/components/utils";

export default async function Page() {
  const data = await getData(Path.related_products);

  return (
    <div className="">
      <Sl />
      <div className="max-w-[1162px] mx-auto">
        {data && <Carousel data={data} title="related products" />}
      </div>
    </div>
  );
}
