import { ButtonHTMLAttributes, ReactNode } from "react"

type ButtonVariant = "default" | "inverse"

type ButtonVariantProps = {
    classes: string
}

type CustomButtonProps = ButtonHTMLAttributes<HTMLButtonElement> & {
    text: string,
    icon?: ReactNode,
    isLoading?: boolean
    variant?: ButtonVariant
}

export function CustomButton({
    text,
    icon,
    variant = "default",
    className,
    isLoading,
    children,
    ...props
}: CustomButtonProps) {
    const variantsProps: Record<ButtonVariant, ButtonVariantProps> = {
        default: {
            classes: "bg-gradient-to-r from-blue-gradient to-purple-gradient text-white"
        },
        inverse: {
            classes: (
                "bg-gradient-to-r from-blue-gradient to-purple-gradient text-transparent bg-clip-border-area border border-1 border-transparent"
                + " [&>span]:bg-gradient-to-r [&>span]:from-blue-gradient [&>span]:to-purple-gradient [&>span]:bg-clip-text"
            )
        }
    }

    const classes = "items-center w-fit p-3 rounded-md flex gap-2 disabled:bg-slate-700 disabled:bg-none disabled:text-slate-400"
        + ` ${variantsProps[variant].classes}`
        + ` ${className}`

    return (
        <button
            className={classes}
            type="button"
            {...props}
        >
            <span>{text}</span>
            {icon}
        </button>
    );
}
