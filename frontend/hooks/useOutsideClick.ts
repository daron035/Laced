import { useEffect, useCallback, RefObject } from "react";

const MOUSE_UP = "mouseup";

function useOutsideClick(handleClose: () => void, ref: RefObject<HTMLElement>) {
  const handleClick = useCallback(
    (event: MouseEvent) => {
      if (
        ref?.current?.contains &&
        !ref.current.contains(event.target as Node)
      ) {
        handleClose();
      }
    },
    [handleClose, ref],
  );

  useEffect(() => {
    document.addEventListener(MOUSE_UP, handleClick);

    return () => {
      document.removeEventListener(MOUSE_UP, handleClick);
    };
  }, [handleClick]);
}

export default useOutsideClick;
