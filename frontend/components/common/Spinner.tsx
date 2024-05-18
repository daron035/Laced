import cn from "classnames";
import { ImSpinner3, ImSpinner2 } from "react-icons/im";

interface Props {
  sm?: boolean;
  md?: boolean;
  lg?: boolean;
}

export default function Spinner({ sm, md, lg }: Props) {
  const className = cn("animate-spin text-white-300 fill-white-300 my-8", {
    "w-4 h-4": sm,
    "w-8 h-8": md,
    "w-10 h-10": lg,
  });

  return (
    <div role="status">
      <ImSpinner2 className={className} />
      <span className="sr-only">Loading...</span>
    </div>
  );
}
