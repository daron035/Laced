import cn from "classnames";

interface Props {
  provider: "google" | "vk";
  children: React.ReactNode;
  [rest: string]: any;
}

export default function SocialButton({ provider, children, ...rest }: Props) {
  const className = cn("flex-1 text-white rounded-md px-3 py-2 font-medium", {
    "bg-red-600 hover:bg-red-500": provider === "google",
    "bg-blue-600 hover:bg-blue-500": provider === "vk",
  });

  return (
    <button className={className} {...rest}>
      <span className="flex justify-start items-center">{children}</span>
    </button>
  );
}
