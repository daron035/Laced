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
    "text-center rounded cursor-pointer select-none",
    {
      "text-white bg-[#101010] hover:bg-[#656667] duration-200":
        action === "black",
      "text-[#101010] border border-[#ADAEAF] hover:bg-slate-200 duration-200":
        action === "white",
    },
    { "py-2 px-4 capitalize": sm },
    { "py-4 px-8 w-auto inline-block uppercase": md },
    { "py-4 uppercase": lg },
  );
  return (
    <div className={className} {...rest}>
      {title}
    </div>
  );
}
