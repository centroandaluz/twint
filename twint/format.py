import logging as logme

def Tweet(config, t):
    if config.Format:
        logme.debug(__name__+':Tweet:Format')
        output = config.Format.replace("{id}", t.id_str)
        output = output.replace("{conversation_id}", t.conversation_id)
        output = output.replace("{date}", t.datestamp)
        output = output.replace("{time}", t.timestamp)
        output = output.replace("{user_id}", t.user_id_str)
        output = output.replace("{username}", t.username)
        output = output.replace("{name}", t.name)
        output = output.replace("{place}", t.place)
        output = output.replace("{timezone}", t.timezone)
        output = output.replace("{urls}", ",".join(t.urls))
        output = output.replace("{photos}", ",".join(t.photos))
        output = output.replace("{video}", str(t.video))
        output = output.replace("{tweet}", t.tweet)
        output = output.replace("{hashtags}", ",".join(t.hashtags))
        output = output.replace("{cashtags}", ",".join(t.cashtags))
        output = output.replace("{replies}", t.replies_count)
        output = output.replace("{retweets}", t.retweets_count)
        output = output.replace("{likes}", t.likes_count)
        output = output.replace("{link}", t.link)
        output = output.replace("{is_retweet}", str(t.retweet))
        output = output.replace("{user_rt_id}", str(t.user_rt_id))
        output = output.replace("{quote_url}", t.quote_url)
        output = output.replace("{near}", t.near)
        output = output.replace("{geo}", t.geo)
        output = output.replace("{mentions}", ",".join(t.mentions))
    else:
        logme.debug(__name__+':Tweet:notFormat')
        output = f"{t.id_str} {t.datestamp} {t.timestamp} {t.timezone} "

        if t.retweet == 1:
           output += "RT "

        output += f"<{t.username}> {t.tweet}"

        if config.Show_hashtags:
            hashtags = ",".join(t.hashtags)
            output += f" {hashtags}"
        if config.Show_cashtags:
            cashtags = ",".join(t.cashtags)
            output += f" {cashtags}"
        if config.Stats:
            output += f" | {t.replies_count} replies {t.retweets_count} retweets {t.likes_count} likes"

    return output

def User(_format, u):
    if _format:
        logme.debug(__name__+':User:Format')
        output = _format.replace("{id}", u.id)
        output += output.replace("{name}", u.name)
        output += output.replace("{username}", u.username)
        output += output.replace("{bio}", u.bio)
        output += output.replace("{location}", u.location)
        output += output.replace("{url}", u.url)
        output += output.replace("{join_date}", u.join_date)
        output += output.replace("{join_time}", u.join_time)
        output += output.replace("{tweets}", u.tweets)
        output += output.replace("{following}", u.following)
        output += output.replace("{followers}", u.followers)
        output += output.replace("{likes}", u.likes)
        output += output.replace("{media}", str(u.media_count))
        output += output.replace("{private}", str(u.is_private))
        output += output.replace("{verified}", str(u.is_verified))
        output += output.replace("{avatar}", u.avatar)
    else:
        logme.debug(__name__+':User:notFormat')
        output = f"{u.id} | {u.name} | @{u.username} | Private: "
        output += f"{u.is_private} | Verified: {u.is_verified} |"
        output += f" Bio: {u.bio} | Location: {u.location} | Url: "
        output += f"{u.url} | Joined: {u.join_date} {u.join_time} "
        output += f"| Tweets: {u.tweets} | Following: {u.following}"
        output += f" | Followers: {u.followers} | Likes: {u.likes} "
        output += f"| Media: {u.media_count} | Avatar: {u.avatar}"

    return output
