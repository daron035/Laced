import Carousel from "@/components/common/Carousel";
import Slider from "@/components/common/Slider";
import Sl from "@/components/common/Sl";

async function getData() {
  // const res = await fetch(`${process.env.NEXT_PUBLIC_HOST}/api/product/`, {
  // const res = await fetch("http://127.0.0.1:8080/api/product/", {
  // const res = await fetch("backend/api/product/", {
  // const res = await fetch("http://django_server/api/product/", {
  // const res = await fetch(rocess.env.NEXT_PUBLIC_HOST + "/api/product/", {
  // const res = await fetch("/api/product/", {
  // const res = await fetch("http://127.0.0.1:8000/api/product/", {
  // django docker container
  const res = await fetch("http://django:8000/api/product/", {
    cache: "no-store",
  });
  // The return value is *not* serialized
  // You can return Date, Map, Set, etc.

  if (!res.ok) {
    // This will activate the closest `error.js` Error Boundary
    throw new Error("Failed to fetch data");
  }

  return res.json();
}

export default async function Page() {
  const data = await getData();

  return (
    <div className="">
      <Sl />
      <div className="max-w-[1162px] mx-auto">
        {data.results && <Carousel data={data.results} title="most popular" />}
      </div>
    </div>
  );
}
