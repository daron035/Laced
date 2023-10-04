import { ChangeEvent, FormEvent } from "react";
import { Input } from "@/components/forms";

interface Config {
  labelText: string;
  labelId: string;
  type: string;
  value: string;
  required?: boolean;
}

interface Props {
  config: Config[];
  isLoading: boolean;
  btnText: string;
  checkBox?: boolean;
  onChange: (event: ChangeEvent<HTMLInputElement>) => void;
  onSubmit: (event: FormEvent<HTMLFormElement>) => void;
}

export default function Form({
  config,
  isLoading,
  btnText,
  checkBox = false,
  onChange,
  onSubmit,
}: Props) {
  return (
    <form className="mb-[26px]" onSubmit={onSubmit}>
      {config.map((input) => (
        <Input
          key={input.labelId}
          labelId={input.labelId}
          type={input.type}
          onChange={onChange}
          value={input.value}
          required={input.required}
        >
          {input.labelText}
        </Input>
      ))}
      {checkBox && (
        <div>
          <input
            className="mr-[13px] accent-black outline-[#D0D0D0]"
            type="checkbox"
            id="check"
          />
          <label className="text-[#101010] text-sm" htmlFor="check">
            Remember Me
          </label>
        </div>
      )}
      <div className="mt-[20px]">
        <input
          className={`w-full text-white py-[16px] cursor-pointer text-lg tracking-wider ${
            isLoading
              ? "!bg-[#EBE9E3] hover:bg-[#656667]"
              : "bg-[#101010] duration-200"
          } hover:bg-[#656667] duration-200`}
          name="check"
          type="submit"
          value={btnText}
        />
      </div>
    </form>
  );
}
