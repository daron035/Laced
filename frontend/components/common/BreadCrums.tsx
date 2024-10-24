import Link from "next/link";
import { IoChevronBackOutline } from "react-icons/io5";

export default function BreadCrums({ item }: { item: string }) {
  return (
    <Link href=".">
      <div className="mb-6 flex items-center gap-x-1 cursor-pointer">
        <span>
          <IoChevronBackOutline size={12} style={{ color: "#101010" }} />
        </span>
        <span className="text-xs">{item}</span>
      </div>
    </Link>
  );
}
