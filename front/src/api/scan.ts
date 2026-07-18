import { customFetch } from "./api"

export function getIP(host: string) {
    return customFetch(`/ip?host=${host}`, {method: 'GET'})
}

export function getWhatweb(url: string) {
    return customFetch(`/whatweb?url=${url}`, {method: 'GET'})
}

export function getReverseDNS(ip: string) {
    return customFetch(`/reverse_dns?ip=${ip}`, {method: 'GET'})
}

export function getSubDNS(host: string) {
    return customFetch(`/sub_dns?host=${host}`, {method: 'GET'})
}

export function getWhoIs(ip: string) {
    return customFetch(`/whois?ip=${ip}`, {method: 'GET'})
}

export function getBanner(url: string) {
    return customFetch(`/banner?url=${url}`, {method: 'GET'})
}

export function getDirectoryScan(domain: string) {
    return customFetch(`/directory_scan?domain=${domain}`, {method: 'GET'})
}

export function getPorts(ip: string) {
    return customFetch(`/ports?ip=${ip}`, {method: 'GET'})
}
