position={
    "职位":{"曹操","刘备","孙权"},
    "技术":{"曹操","刘备","张飞","关羽"}
}

print(position["职位"]&position["技术"])

print(position["职位"]-position["技术"])

print(position["技术"]-position["职位"])

print(position["职位"]^position["技术"])

print(position["职位"]|position["技术"])

