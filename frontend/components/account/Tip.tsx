// // import SuggestionItem from "@/components/account/SuggestionItem";
// // import { useRetrieveSaleItemsQuery } from "@/redux/features/saleApiSlice";
// //
// // export default function Tip() {
// //   const { data: i } = useRetrieveSaleItemsQuery({ style_codes: "ID2349" });
// //   return (
// //     <div>
// //       {i &&
// //         i.results.map((item, index) => {
// //           return (
// //             <SuggestionItem
// //               key={index}
// //               name={item.name}
// //               image={item.image}
// //               year_released={item.year_released}
// //               sku={item.sku}
// //             />
// //           );
// //         })}
// //     </div>
// //   );
// // }

// import SuggestionItem from "@/components/account/SuggestionItem";
// import { useRetrieveSaleItemsQuery } from "@/redux/features/saleApiSlice";

// export default function Tip({ handleOnStatusClick }) {
//   const { data } = useRetrieveSaleItemsQuery({});
//   console.log(data);
//   const filteredResults = data?.results.filter(item => item.sku !== 'ID2350');

//   return (
//     <div>
//       {filteredResults &&
//         filteredResults.results.map((item, index) => {
//           return (
//             <SuggestionItem
//               key={index}
//               name={item.name}
//               image={item.image}
//               year_released={item.year_released}
//               sku={item.sku}
//               handleOnStatusClick={handleOnStatusClick}
//             />
//           );
//         })}
//     </div>
//   );
// }

import SuggestionItem from "@/components/account/SuggestionItem";
import { useRetrieveSaleItemsQuery } from "@/redux/features/saleApiSlice";

export default function Tip({ style_codes, handleOnStatusClick }) {
  const { data } = useRetrieveSaleItemsQuery({});
  // console.log(data);

  // Filter out items with SKU 'ID34550'
  const excludedStyleCodes = style_codes ? style_codes.split(',') : [];
  // const filteredResults = data?.results.filter(item => item.sku !== 'ID2350');
  const filteredResults = data?.results.filter(item => !excludedStyleCodes.includes(item.sku));

  return (
    <div>
      {filteredResults &&
        filteredResults.map((item, index) => (
          <SuggestionItem
            key={index}
            name={item.name}
            image={item.image}
            year_released={item.year_released}
            sku={item.sku}
            handleOnStatusClick={handleOnStatusClick}
          />
        ))}
    </div>
  );
}
