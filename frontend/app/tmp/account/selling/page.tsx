"use client";

import Header from "@/components/account/Header";
import { Search } from "@/components/common/svgs";
import React, { useEffect, useState } from "react";

import tabItem from "@/components/selling/tabItem";
import { useRetrieveSaleItemsQuery } from "@/redux/features/saleApiSlice";

const tabs = [
  { id: 0, label: "Pending", link: "asdf" },
  { id: 1, label: "Active", link: "http://localhost:8000/api/product/" },
  {
    id: 2,
    label: "Completed",
    link: "https://jsonplaceholder.typicode.com/users/",
  },
  { id: 3, label: "Cancelled", link: "#" },
];

const noRes = (
  <div className="pb-4 border-b">
    <div className="mt-24 mb-48">
      <Search width="24px" height="24px" className="fill-gray-500 mx-auto" />
      <h3 className="uppercase text-gray-950 text-center text-lg mt-1">
        No results found
      </h3>
      <p className=" text-center mt-1">Sorry, we couldn't find any products.</p>
    </div>
  </div>
);

export default function Page() {
  const { data, isLoading, isSuccess } = useRetrieveSaleItemsQuery();

  const [activeTab, setActiveTab] = useState(0);
  const [tabData, setTabData] = useState([]);

  useEffect(() => {
    data;
  }, [activeTab]);

  return (
    <div className="w-[960px] pt-12 pb-24 px-10 mx-auto">
      <Header button title="Your Sale Items" breadCrum="Account" />
      <ul className="mb-6 flex justify-between border-b">
        {tabs.map((item, index) => {
          return (
            <li
              className={`text-gray-950 text-xs pb-3 relative cursor-pointer mr-6 ${
                index === activeTab
                  ? "after:absolute after:block after:border-b after:border-gray-950 after:w-full after:-bottom-[1px]"
                  : ""
              }`}
              onClick={(e) => {
                e.preventDefault();
                setActiveTab(index);
              }}
            >
              <a href={item.link}>{item.label} (0)</a>
            </li>
          );
        })}
      </ul>
      <div className="flex flex-col gap-y-8">
        <div className="relative">
          <Search
            width="16px"
            height="16px"
            className="absolute fill-gray-500 top-1/2 -translate-y-1/2 left-5"
          />
          <input
            className="border border-gray-400 rounded-full py-4 pl-12 pr-6 bg-transparent w-full shadow-none
                        focus:outline-none focus:border-gray-950 ease-in duration-200 text-gray-950
                        focus:text-gray-950"
            placeholder="Search"
          />
        </div>
        <ul className="p-8 bg-white flex flex-col gap-y-4">
          {data &&
            data.results.map((item, index) => (
              <React.Fragment key={index}>{tabItem(item)}</React.Fragment>
            ))}
          {!isSuccess && noRes}
        </ul>
      </div>
      <nav className="my-6 flex justify-center">
        <button className="py-2 px-3 text-gray-950 text-xs border-2 border-gray-950 leading-none">
          1
        </button>
      </nav>
    </div>
  );
}
// const fetchData = async () => {
//   try {
//     const response = await fetch(tabs[activeTab].link, {
//       method: "GET",
//       headers: {
//         Accept: "application/json",
//       },
//       credentials: "include",
//     });
//
//     if (!response.ok) {
//       // Handle non-OK responses, e.g., redirect or show an error message
//       console.error("Request failed with status:", response.status);
//       return;
//     }
//
//     const data = await response.json();
//     setTabData(data);
//   } catch (error) {
//     setTabData([]);
//     console.error("Error fetching data:", error);
//   }
// };
//
// fetchData();
// console.log(data[0].name);
//
//
//
//
// {tabData.length > 0
//   ? tabData.map((item, index) => (
//       <React.Fragment key={index}>{tabItem(item)}</React.Fragment>
//     ))
//   : noRes}
