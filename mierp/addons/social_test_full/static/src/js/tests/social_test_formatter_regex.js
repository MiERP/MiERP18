/** @mierp-module */

import { SocialPostFormatterMixinBase } from '@social/js/social_post_formatter_mixin';

import { patchWithCleanup } from "@web/../tests/helpers/utils";

QUnit.module('Social Formatter Regex', {}, () => {
    QUnit.test('Facebook Message', (assert) => {
        assert.expect(1);

        patchWithCleanup(SocialPostFormatterMixinBase, {
            _getMediaType() { return 'facebook' },
            _formatPost() {
                this.originalPost = { account_id: { raw_value: 42 } };
                return super._formatPost(...arguments);
            }
        });

        const testMessage = 'Hello @[542132] mierp-Social, check this out: 127.0.0.1:8730?utm=mail&param=1 #crazydeals #mierp';
        const finalMessage = SocialPostFormatterMixinBase._formatPost(testMessage);

        assert.equal(finalMessage, [
            "Hello",
            "<a href='/social_facebook/redirect_to_profile/42/542132?name=mierp-Social' target='_blank'>mierp-Social</a>,",
            "check this out:",
            "<a href='127.0.0.1:8730?utm=mail&amp;param=1' class='text-truncate' target='_blank' rel='noreferrer noopener'>127.0.0.1:8730?utm=mail&amp;param=1</a>",
            "<a href='https://www.facebook.com/hashtag/crazydeals' target='_blank'>#crazydeals</a>",
            "<a href='https://www.facebook.com/hashtag/mierp' target='_blank'>#mierp</a>",
        ].join(' '));
    });

    QUnit.test('Instagram Message', (assert) => {
        assert.expect(1);

        patchWithCleanup(SocialPostFormatterMixinBase, {
            _getMediaType() { return 'instagram' },
        });

        const testMessage = 'Hello @mierp.Social, check this out: 127.0.0.1:8730 #crazydeals #mierp';
        const finalMessage = SocialPostFormatterMixinBase._formatPost(testMessage);

        assert.equal(finalMessage, [
            "Hello",
            "<a href='https://www.instagram.com/mierp.Social' target='_blank'>@mierp.Social</a>,",
            "check this out:",
            "<a href='127.0.0.1:8730' class='text-truncate' target='_blank' rel='noreferrer noopener'>127.0.0.1:8730</a>",
            "<a href='https://www.instagram.com/explore/tags/crazydeals' target='_blank'>#crazydeals</a>",
            "<a href='https://www.instagram.com/explore/tags/mierp' target='_blank'>#mierp</a>",
        ].join(' '));
    });

    QUnit.test('LinkedIn Message', (assert) => {
        assert.expect(1);

        patchWithCleanup(SocialPostFormatterMixinBase, {
            _getMediaType() { return 'linkedin' },
        });

        const testMessage = 'Hello, check this out: 127.0.0.1:8730 {hashtag|#|crazydeals} #mierp';
        const finalMessage = SocialPostFormatterMixinBase._formatPost(testMessage);

        assert.equal(finalMessage, [
            "Hello, check this out:",
            "<a href='127.0.0.1:8730' class='text-truncate' target='_blank' rel='noreferrer noopener'>127.0.0.1:8730</a>",
            "<a href='https://www.linkedin.com/feed/hashtag/?keywords=crazydeals' target='_blank'>#crazydeals</a>",
            "<a href='https://www.linkedin.com/feed/hashtag/?keywords=mierp' target='_blank'>#mierp</a>",
        ].join(' '));
    });

    QUnit.test('Twitter Message', (assert) => {
        assert.expect(1);

        patchWithCleanup(SocialPostFormatterMixinBase, {
            _getMediaType() { return 'twitter' },
        });

        const testMessage = 'Hello @mierp-Social, check this out: 127.0.0.1:8730 #crazydeals #mierp';
        const finalMessage = SocialPostFormatterMixinBase._formatPost(testMessage);

        assert.equal(finalMessage, [
            "Hello",
            "<a href='https://twitter.com/mierp-Social' target='_blank'>@mierp-Social</a>,",
            "check this out:",
            "<a href='127.0.0.1:8730' class='text-truncate' target='_blank' rel='noreferrer noopener'>127.0.0.1:8730</a>",
            "<a href='https://twitter.com/hashtag/crazydeals?src=hash' target='_blank'>#crazydeals</a>",
            "<a href='https://twitter.com/hashtag/mierp?src=hash' target='_blank'>#mierp</a>",
        ].join(' '));
    });

    QUnit.test('YouTube Message', (assert) => {
        assert.expect(1);

        patchWithCleanup(SocialPostFormatterMixinBase, {
            _getMediaType() { return 'youtube' },
        });

        const testMessage = 'Hello, check this out: 127.0.0.1:8730 #crazydeals #mierp';
        const finalMessage = SocialPostFormatterMixinBase._formatPost(testMessage);

        assert.equal(finalMessage, [
            "Hello, check this out:",
            "<a href='127.0.0.1:8730' class='text-truncate' target='_blank' rel='noreferrer noopener'>127.0.0.1:8730</a>",
            "<a href='https://www.youtube.com/results?search_query=%23crazydeals' target='_blank'>#crazydeals</a>",
            "<a href='https://www.youtube.com/results?search_query=%23mierp' target='_blank'>#mierp</a>",
        ].join(' '));
    });
});
