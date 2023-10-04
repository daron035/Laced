import { ChangeEvent } from "react";

interface Props {
  labelId: string;
  type: string;
  onChange: (event: ChangeEvent<HTMLInputElement>) => void;
  value: string;
  children: React.ReactNode;
  required?: boolean;
}
export default function Input({
  labelId,
  type,
  onChange,
  value,
  children,
  required = false,
}: Props) {
  return (
    <div className="mb-[24px]">
      <label className="text-xs text-[#777777] mb-[6px] " htmlFor={labelId}>
        {children}
      </label>
      <input
        id={labelId}
        className="bg-transparent border-[1px] border-[#ADAEAF] rounded text-black
              w-full p-[14px] focus-visible:outline focus-visible:outline-[#101010]"
        name={labelId}
        type={type}
        onChange={onChange}
        value={value}
        required={required}
      />
    </div>
  );
}
