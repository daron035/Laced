import Link from "next/link";
import { GeneralButton } from "@/components/common";
import Header from "@/components/account/Header";
import { AddressDetailForm } from "@/components/forms";
import type { Metadata } from "next";
import { SocialButtons } from "@/components/common";

export const metadata: Metadata = {
  title: "Register",
  description: "Register page",
};

export default function Page() {
  return (
    <main>
      <div className="w-[880px] mx-auto px-[40px] pt-[80px] pb-[100px]">
        <Header button={false} title="Address" breadCrum="Your Account" />

        <div className=" p-10 bg-white">
          <div className="flex justify-between pb-6 mb-6 border-b text-[#656667]">
            <div className="">
              <p className="font-semibold leading-6">First name Last name</p>
              <p className="leading-6">House Number / Name</p>
              <p className="leading-6">City</p>
              <p className="leading-6">County iso</p>
              <p className="leading-6">Postal code</p>
            </div>
            <div className="flex gap-2 items-center text-sm">
              <GeneralButton
                sm
                action="white"
                title="Edit"
                style={{ padding: "4px 12px" }}
                // onClick={() => callbackClose()}
                // onClick={callbackClose}
              />
              <GeneralButton
                sm
                action="white"
                title="Delete"
                style={{ padding: "4px 12px" }}
                // onClick={() => callbackClose()}
                // onClick={callbackClose}
              />
            </div>
          </div>
          <Link href="#" className="text-gray-950 underline hover:no-underline">
            Add Address
          </Link>
        </div>
      </div>
    </main>
  );
}
