import { getImgURL } from "@/utils/image.utils";
import ImageWithFallback from "@/utils/ImageWithFallback";

interface Props {
  name: string;
  image: string;
  year_released: number; // Add year_released prop
  sku: string;
  handleOnStatusClick: (value: string | undefined) => void;
  queryString: string | null;
}

export default function SuggestionItem({
  name,
  image,
  year_released,
  sku,
  handleOnStatusClick,
  queryString,
}: Props) {
  const imageUrl = getImgURL(image, "100:100");

  return (
    <>
      <div className="py-3 flex items-center border-t border-gray-300 text-gray-950 text-xs">
        <ImageWithFallback
          src={imageUrl}
          width={64}
          height={64}
          alt=""
          className="mr-4"
        />
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
