import Link from "next/link";
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
      <div className="w-[780px] mx-auto px-[40px] pt-[80px] pb-[100px]">
        <Header button={false} title="Address Details" breadCrum="Back" />

        <AddressDetailForm />
      </div>
    </main>
  );
}
