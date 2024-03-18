import { IoChevronBackOutline, IoChevronForwardOutline } from "react-icons/io5";

export default function BreadCrums({ item }: { item: string }) {
  return (
    <div className="mb-6 flex items-center gap-x-1">
      <span>
        <IoChevronBackOutline
          size={12}
          style={{ color: "#101010" }}
          className="cursor-pointer"
        />
      </span>
      <span className="text-xs">{item}</span>
    </div>
  );
}
