import Link from "next/link";
import { RegisterForm } from "@/components/forms";
import type { Metadata } from "next";
import { SocialButtons } from "@/components/common";

export const metadata: Metadata = {
  title: "Register",
  description: "Register page",
};

export default function Page() {
  return (
    <main>
      <div className="w-[560px] mx-auto px-[40px] pt-[80px] pb-[100px]">
        <h1 className="mb-[24px] text-[#101010] uppercase font-medium text-4xl tracking-wide subpixel-antialiased">
          Register
        </h1>

        <RegisterForm />

        <SocialButtons />

        <p className="text-sm text-[#101010] tracking-tight font-semibold underline">
          <Link href="#" className="pr-[10px] mr-[10px] border-r-[1px]">
            Sign Up
          </Link>
          <Link href="#" className="pr-[10px] mr-[10px] border-r-[1px]">
            Forgot Your Password?
          </Link>
          <Link href="#">Didn&#39;t Receive Confimation Instructions?</Link>
        </p>
      </div>
    </main>
  );
}
