import cn from "classnames";

interface Props {
  action: "black" | "white";
  title: string;
  sm?: boolean;
  md?: boolean;
  lg?: boolean;
  [rest: string]: any;
}

export default function GeneralButton({
  action,
  title,
  sm,
  md,
  lg,
  ...rest
}: Props) {
  const className = cn(
    "uppercase text-center rounded cursor-pointer",
    {
      "text-white bg-[#101010] hover:bg-[#656667] duration-200":
        action === "black",
      "text-[#101010] border border-[#ADAEAF] hover:bg-slate-200 duration-200":
        action === "white",
    },
    { "py-4": sm },
    { "py-4 px-8 w-auto inline-block": md },
    { "py-4": lg },
  );
  return (
    <div className={className} {...rest}>
      {title}
    </div>
  );
}
