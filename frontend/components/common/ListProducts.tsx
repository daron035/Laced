"use client";

import ListProduct from "@/components/common/ListProduct";
import styles from "@/styles/listProduct.module.scss";
import { useCallback, useEffect, useState } from "react";

export default function Page() {
  const [products, setProducts] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [fetching, setFetching] = useState(true);
  const [totalCount, setTotalCount] = useState(0);

  useEffect(() => {
    if (fetching) {
      fetch(
        `${process.env.NEXT_PUBLIC_HOST}/api/product/?page=${currentPage}`,
        {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
          },
          credentials: "include",
        },
      )
        .then((response) => {
          if (!response.ok) {
            throw new Error(
              "Network response was not ok " + response.statusText,
            );
          }
          return response.json();
        })
        .then((data) => {
          setProducts((prevProducts) => [...prevProducts, ...data.results]);
          setCurrentPage((prevState) => prevState + 1);
          setTotalCount(data.count);
        })
        .catch((error) => {
          console.error(
            "There has been a problem with your fetch operation:",
            error,
          );
        })
        .finally(() => setFetching(false));
    }
  }, [fetching]);

  const scrollHandler = useCallback(() => {
    if (
      document.documentElement.scrollHeight -
        (document.documentElement.scrollTop + window.innerHeight) <
        250 &&
      products.length < totalCount
    ) {
      setFetching(true);
    }
  }, [products.length, totalCount]);

  useEffect(() => {
    document.addEventListener("scroll", scrollHandler);
    return () => {
      document.removeEventListener("scroll", scrollHandler);
    };
  }, [scrollHandler]);

  return (
    <div className={styles.container}>
      {products.map((item, index) => (
        <ListProduct item={item} />
      ))}
    </div>
  );
}
