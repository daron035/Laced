import ListProduct from "@/components/common/ListProduct";
import styles from "@/styles/listProduct.module.scss";

const count = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16];

export default function Page() {
  return (
    <div className={styles.container}>
      {count.map((item, index) => (
        <ListProduct key={item} item={index} />
      ))}
    </div>
  );
}
