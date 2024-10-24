"use client";

import { Form } from "@/components/forms";
import { GeneralButton } from "@/components/common";

export default function RegisterForm() {
  const config = [
    {
      labelText: "First name",
      labelId: "first_name",
      type: "text",
      value: "first_name",
      required: true,
    },
    {
      labelText: "Last name",
      labelId: "last_name",
      type: "text",
      value: "last_name",
      required: true,
    },
    {
      labelText: "Email address",
      labelId: "email",
      type: "email",
      value: "email",
      required: true,
    },
    {
      labelText: "Password",
      labelId: "password",
      type: "password",
      value: "password",
      required: true,
    },
    {
      labelText: "Re-enter Password",
      labelId: "re_password",
      type: "password",
      value: "re_password",
      required: true,
    },
  ];
  return (
    // <form className="mb-[26px]" onSubmit={onSubmit}>
    <form className="mb-[26px] bg-white">
      <div className="p-10">
        <div className="flex gap-4">
          <div className="mb-[24px]">
            <label
              className="text-xs text-[#777777] mb-[6px] "
              htmlFor="first_name"
            >
              First name
            </label>
            <input
              id="first_name"
              className="bg-transparent border-[1px] border-[#ADAEAF] rounded text-black
                w-full p-[14px] focus-visible:outline focus-visible:outline-[#101010]"
              name="address[first_name]"
              type="text"
              // onChange={onChange}
              // value={value}
              // required={required}
            />
          </div>
          <div className="mb-[24px]">
            <label
              className="text-xs text-[#777777] mb-[6px] "
              htmlFor="last_name"
            >
              Last name
            </label>
            <input
              id="last_name"
              className="bg-transparent border-[1px] border-[#ADAEAF] rounded text-black
                w-full p-[14px] focus-visible:outline focus-visible:outline-[#101010]"
              name="address[last_name]"
              type="text"
              // onChange={onChange}
              // value={value}
              // required={required}
            />
          </div>
        </div>
        <hr className="mb-6" />
        {/* Input */}
        <div className="mb-[24px]">
          <label className="text-xs text-[#777777] mb-[6px] " htmlFor="country">
            Country
          </label>
          <input
            id="country"
            className="bg-transparent border-[1px] border-[#ADAEAF] rounded text-black
                w-full p-[14px] focus-visible:outline focus-visible:outline-[#101010]"
            name="address[country]"
            type="text"
            // onChange={onChange}
            // value={value}
            // required={required}
          />
        </div>
        <div className="mb-[24px]">
          <label
            className="text-xs text-[#777777] mb-[6px] "
            htmlFor="house_name_or_number"
          >
            House Number / Name
          </label>
          <input
            id="house_name_or_number"
            className="bg-transparent border-[1px] border-[#ADAEAF] rounded text-black
                w-full p-[14px] focus-visible:outline focus-visible:outline-[#101010]"
            name="address[house_name_or_number]"
            type="text"
            // onChange={onChange}
            // value={value}
            // required={required}
          />
        </div>
        <div className="mb-[24px]">
          <label className="text-xs text-[#777777] mb-[6px] " htmlFor="address">
            Address
          </label>
          <input
            id="address"
            className="bg-transparent border-[1px] border-[#ADAEAF] rounded text-black
                w-full p-[14px] focus-visible:outline focus-visible:outline-[#101010]"
            name="address[address]"
            type="text"
            // onChange={onChange}
            // value={value}
            // required={required}
          />
        </div>
        <div className="mb-[24px]">
          <label className="text-xs text-[#777777] mb-[6px] " htmlFor="city">
            City
          </label>
          <input
            id="city"
            className="bg-transparent border-[1px] border-[#ADAEAF] rounded text-black
                w-full p-[14px] focus-visible:outline focus-visible:outline-[#101010]"
            name="address[city]"
            type="text"
            // onChange={onChange}
            // value={value}
            // required={required}
          />
        </div>
        <div className="mb-[24px]">
          <label
            className="text-xs text-[#777777] mb-[6px] "
            htmlFor="postcode"
          >
            Postcode
          </label>
          <input
            id="postcode"
            className="bg-transparent border-[1px] border-[#ADAEAF] rounded text-black
                w-full p-[14px] focus-visible:outline focus-visible:outline-[#101010]"
            name="address[postcode]"
            type="text"
            // onChange={onChange}
            // value={value}
            // required={required}
          />
        </div>

        <div>
          <input
            className="mr-[13px] accent-black outline-[#D0D0D0]"
            type="checkbox"
            id="check"
          />
          <label className="text-[#101010] text-xs" htmlFor="primary_address">
            This is my primary address
          </label>
        </div>

        <div className="flex justify-end gap-6 mt-8">
          <GeneralButton
            md
            action="white"
            title="Cancel"
            style={{ borderWidth: "0px" }}
            // onClick={() => callbackClose()}
            // onClick={callbackClose}
          />
          <GeneralButton
            md
            action="black"
            title="Save Changes"
            // onClick={() => callbackClose()}
            // onClick={callbackClose}
          />
        </div>
        {/* <div className="mt-[20px]">
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
      </div> */}
      </div>
    </form>
  );
}
