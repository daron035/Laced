"use client";
import SuggestionItem from "@/components/account/SuggestionItem";

import { useRetrieveSaleItemsQuery } from "@/redux/features/saleApiSlice";
import Link from "next/link";
import { Search } from "@/components/common/svgs";
import Header from "@/components/account/Header";
import GeneralButton from "@/components/common/GeneralButton";
import { useQueryParams } from "@/hooks";
import { useCallback, useState, useRef, useEffect } from "react";
import { useRouter } from "next/navigation";
import Tip from "@/components/account/Tip";

export default function Page() {
  const router = useRouter();
  // Generic
  const { queryParams, setQueryParams } = useQueryParams<{
    style_codes?: string;
  }>();

  const style_codes = queryParams.get("style_codes");
  // console.log('sdf',style_codes)

  const q = style_codes
    ? { style_codes: style_codes }
    : ({} as { style_codes?: string | null });

  // console.log(q);
  const { data, isSuccess } = useRetrieveSaleItemsQuery(q);
  // const { data: h } = useRetrieveSaleItemsQuery({});

  const queryStringParams = queryParams.get("style_codes");

  const handleOnStatusClick = useCallback(
    (value: string | undefined) => {
      if (value === queryStringParams || !value) {
        console.log(0);
        console.log(value);
        setQueryParams({
          style_codes: undefined,
        });
        return;
      }

      const queryString = queryParams.get("style_codes");

      if (queryString) {
        const valuesArray = queryString.split(","); // Разбиваем строку на массив значений

        if (valuesArray.includes(value)) {
          // Если значение уже существует в массиве, удаляем его
          const updatedValues = valuesArray.filter((val) => val !== value);
          setQueryParams({ style_codes: updatedValues.join(",") });
        } else {
          // Если значения нет в массиве, добавляем его
          const updatedValues = [...valuesArray, value];
          setQueryParams({ style_codes: updatedValues.join(",") });
        }
      } else {
        // Если строки нет, устанавливаем значение в качестве первого
        setQueryParams({ style_codes: value });
      }
    },

    [setQueryParams, queryStringParams],
  );

  return (
    <>
      <Header button={false} title="sell items" breadCrum="Selling" />
      <div className="flex flex-col gap-y-8">
        {!style_codes && (
          <div className="relative">
            <Search
              width="16px"
              height="16px"
              className="absolute fill-gray-500 top-1/2 -translate-y-1/2 left-5"
            />
            <form action="">
              <input
                className="border border-gray-400 rounded-full py-4 pl-12 pr-6 bg-transparent w-full shadow-none
                        focus:outline-none focus:border-gray-950 ease-in duration-200 text-gray-950
                        focus:text-gray-950"
                placeholder="Item name, brand, code or style"
              />
            </form>
          </div>
        )}
        <div>
          {!style_codes && (
            <div className="uppercase text-gray-950 text-sm pb-4">
              Suggestions
            </div>
          )}
          {data &&
            data.results.map((item, index) => {
              return (
                <SuggestionItem
                  key={index}
                  name={item.name}
                  image={item.image}
                  year_released={item.year_released}
                  sku={item.sku}
                  handleOnStatusClick={handleOnStatusClick}
                  queryString={style_codes}
                />
              );
            })}
        </div>
      </div>
      {style_codes ? (
        <div className="mt-8 flex gap-x-6">
          <GeneralButton
            sm
            action="white"
            title="Add More"
            style={{
              width: "100%",
            }}
            onClick={() => console.log(3)}
          />
          <Link href={`new/${style_codes}`} style={{ width: "100%" }}>
            <GeneralButton
              lg
              action="black"
              title="Next"
              link="asd"
              style={{ width: "100%", border: "none" }}
            />
          </Link>
        </div>
      ) : (
        <div className="mt-8 flex gap-x-6">
          <GeneralButton
            sm
            action="white"
            title="Cancel"
            style={{
              width: "150px",
              marginLeft: "auto",
              border: "none",
              textDecoration: "underline",
            }}
          />
          <GeneralButton
            lg
            action="black"
            title="Search"
            style={{ width: "300px" }}
          />
        </div>
      )}
      <Tip
        style_codes={style_codes}
        handleOnStatusClick={handleOnStatusClick}
      />
    </>
  );
}
