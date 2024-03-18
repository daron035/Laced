import { getImgURL } from "@/utils/image.utils";
import Image from "next/image";

interface Props {
  name: string;
  image: string;
  item: any;
}

const DifListingSellingButton = (
  <div className="mt-2">
    <span className="text-xs py-2 px-4 border-[1px] border-[#D2202B] rounded-full text-[#D2202B]">
      Failed Verification
    </span>
  </div>
);

export default function tabItem({ name, image }: Props) {
  const imageUrl = getImgURL(image);
  console.log(image);

  return (
    <div className="pb-5 border-b text-gray-950 leading-none">
      <div className="flex flex-row gap-6">
        {image ? (
          <Image src={imageUrl} width={112} height={112} alt="" />
        ) : (
          <Image
            src="/new_balance_650r_white_black_1.jpg"
            width={112}
            height={112}
            alt=""
          />
        )}
        <div className="flex flex-row gap-6 w-full">
          <div className="w-[34%] box-content flex flex-col gap-1">
            <span className="text-sm">{name}</span>
            <span className="text-xs">UK 7.5 | EU 42 | US 8.5</span>
            <span className="text-xs text-[#656667]">DD1391-100</span>
            {DifListingSellingButton}
          </div>
          <div className="w-1/3 flex items-center justify-center">$135</div>
          <div className="w-1/3 flex items-center justify-end ">
            <div className="border-[1px] border-[#ADAEAF] rounded py-1 px-3 text-sm cursor-pointer hover:bg-slate-100 transiotion ease-in-out duration-200">
              View
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
