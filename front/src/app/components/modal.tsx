import React, { ReactNode, useEffect, useRef } from "react"


type ModalProps = {
    isOpen: boolean
    children: ReactNode
    onClose: VoidFunction
}


export function Modal({ isOpen, children, onClose }: ModalProps) {
    const modalRef = useRef<HTMLDivElement>(null);

    useEffect(() => {
        const handleClickOutside = (e: MouseEvent) => {
            if (modalRef.current && !modalRef.current.contains(e.target as Node)) {
                onClose();
            }
        };

        if (isOpen) {
            document.addEventListener("mousedown", handleClickOutside);
        }

        return () => {
            document.removeEventListener("mousedown", handleClickOutside);
        };
    }, [isOpen, onClose]);

    if (!isOpen) {
        return (
            <></>
        )
    }

    return (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
            <div
                className="flex flex-col bg-slate-kali border-blue-kali border-2 p-6 rounded-lg shadow-lg max-w-md w-full text-white"
                ref={modalRef}
            >
                {children}
            </div>
        </div>
    );
}
