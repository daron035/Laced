"use client";
import styles from "../../../styles/carousel.module.scss";
import { useRef } from "react";

export default function Page() {
  const containerRef = useRef<HTMLDivElement>(null);
  const itemWidth = 300; // Ширина каждого элемента
  const itemsPerScroll = 5; // Количество элементов для прокрутки

  const handleNextClick = () => {
    if (containerRef.current) {
      const container = containerRef.current;
      const scrollAmount = itemWidth * itemsPerScroll;

      if (
        container.scrollLeft + container.clientWidth ===
        container.scrollWidth
      ) {
        container.scrollTo({
          left: 0,
          behavior: "smooth",
        });
      } else {
        container.scrollBy({
          left: scrollAmount,
          behavior: "smooth",
        });
      }
    }
  };

  const handlePrevClick = () => {
    if (containerRef.current) {
      const container = containerRef.current;
      const scrollAmount = itemWidth * itemsPerScroll;

      if (container.scrollLeft === 0) {
        container.scrollTo({
          left: container.scrollWidth,
          behavior: "smooth",
        });
      } else {
        container.scrollBy({
          left: -scrollAmount,
          behavior: "smooth",
        });
      }
    }
  };

  // Создаем массив с 20 элементами (можете добавить больше)
  const items = Array.from({ length: 20 }, (_, index) => (
    <div key={index} className={styles.item}>
      {`Item ${index + 1}`}
    </div>
  ));

  return (
    <div>
      <button onClick={handlePrevClick}>Назад</button>
      <button onClick={handleNextClick} className="ml-3">
        Вперед
      </button>
      <div className={styles.scroll_container} ref={containerRef}>
        {items}
      </div>
    </div>
  );
}
