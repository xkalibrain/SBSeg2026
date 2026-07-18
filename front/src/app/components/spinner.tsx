import Image from "next/image"

type SpinnerProps = {
    width?: number
    height?: number
}

export function Spinner({ width, height }: SpinnerProps) {
    return (
        <Image
            className="motion-safe:animate-spin"
            src="/loading.svg"
            alt={""}
            width={width ?? 70}
            height={height ?? 24}
            priority
        />
    )
}
