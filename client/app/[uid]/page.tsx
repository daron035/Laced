"use client";

export default function Page({ params }: { params: { uid: any } }) {
  return <main>{params.uid}</main>;
}
