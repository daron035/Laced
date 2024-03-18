import Image from "next/image";
import { getImgURL } from "@/utils/image.utils";

interface Props {
  name: string;
  image: string;
  handleOnStatusClick: (value: string | undefined) => void;
}

export default function SuggestionItem({
  name,
  image,
  year_released,
  sku,
  handleOnStatusClick,
  queryString,
}: Props) {
  const imageUrl = getImgURL(image);

  return (
    <>
      <div className="py-3 flex items-center border-t border-gray-300 text-gray-950 text-xs">
        <Image src={imageUrl} width={64} height={64} alt="" className="mr-4" />
        <div>
          <div>{name}</div>
          <div className="text-[#656667]">
            {year_released}| {sku}
          </div>
        </div>
        <div
          className="ml-auto border-[1px] border-[#ADAEAF] rounded py-1 px-3 text-sm cursor-pointer hover:bg-slate-100 transiotion ease-in-out duration-200"
          onClick={() => handleOnStatusClick(sku)}
        >
          {queryString ? "Remove" : "Select"}
        </div>
      </div>
    </>
  );
}
